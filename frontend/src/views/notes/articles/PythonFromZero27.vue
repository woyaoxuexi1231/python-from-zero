<template>
  <div class="article">
    <p>
      第 1 课学过 <code>a: int</code>、<code>-&gt; str</code>；第 26 课 dataclass 字段也在写类型。
      这一课补日常最常见的几种：<strong>可能没有</strong>、<strong>多种类型之一</strong>、
      <strong>只能是固定几个值</strong>、<strong>字典的结构说明</strong>。
      接近 Java 的泛型、<code>Optional</code>、枚举字面量——但 Python 标注默认<strong>不拦运行时</strong>，主要给编辑器和检查工具看。
    </p>

    <h2>先记住：标注是说明书，不是运行时警察</h2>
<pre><code>def add(a: int, b: int) -> int:
    return a + b

add(1, 2)       # 3
add("1", "2")   # "12" —— 运行时照样跑，不会 TypeError</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        类型标注主要服务 IDE 补全、mypy、pyright 等静态检查。
        想「查错」要额外跑检查器；不能指望 CPython 因为标注不符就拒绝执行。
        这和 Java 编译期强制类型不同——Python 仍是动态语言，标注是可选的文档层。
      </p>
    </div>

    <h2>容器泛型：list[str]、dict[str, int]</h2>
<pre><code>names: list[str] = ["小明", "hulei"]
scores: dict[str, int] = {"小明": 90}
pair: tuple[int, str] = (1, "A")
many: tuple[int, ...] = (1, 2, 3)   # 长度不定，元素都是 int

def top_scorer(book: dict[str, int]) -> str:
    return max(book, key=book.get)</code></pre>
    <p>
      不只标「是 list」，还要标「装什么」。读代码的人一眼知道：
      <code>book</code> 是「名字 → 分数」，返回值是某个名字（str）。
    </p>

    <h2>T | None / Optional[T]：可能没有</h2>
    <p>第 12 课 <code>get_score</code> 找不到人返回 <code>None</code>，标注应写清楚。</p>
<pre><code>def find_score(book: dict[str, int], name: str) -> int | None:
    return book.get(name)

# 旧写法，等价：
# from typing import Optional
# def find_score(...) -> Optional[int]: ...</code></pre>
    <p>
      调用方看到 <code>| None</code>，就知道要先判断：
      <code>if (s := find_score(book, name)) is not None:</code> 再用。
    </p>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        写了 <code>-&gt; int</code> 却可能返回 <code>None</code>，编辑器不会帮你 runtime 报错，
        但静态检查会警告——这是标注的价值：把「可能没有」写进签名，别藏惊喜。
      </p>
    </div>

    <h2>A | B / Union：多种类型之一</h2>
<pre><code>def double_value(x: int | str) -> int | str:
    if isinstance(x, int):
        return x * 2
    return x + x</code></pre>
    <p>
      参数或返回值可以是几种类型之一。Python 3.10+ 推荐 <code>int | str</code>；
      旧代码常见 <code>Union[int, str]</code>，含义相同。
      运行时仍要靠 <code>isinstance</code> 分支处理，标注不会自动帮你转换。
    </p>

    <h2>Literal：只能是几个固定值</h2>
<pre><code>from typing import Literal

Status = Literal["pending", "done", "cancelled"]

def set_status(task_id: int, status: Status) -> str:
    return f"任务 {task_id} → {status}"</code></pre>
    <p>
      比 <code>str</code> 更窄：只能是 <code>"pending"</code>、<code>"done"</code>、<code>"cancelled"</code> 之一。
      编辑器会提示合法值；传 <code>"running"</code> 静态检查会警告。
      接近「字符串版枚举」，但仍是 str，不是 Enum 类。
    </p>

    <h2>TypedDict：给 dict 定字段表</h2>
<pre><code>from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int

def greet_user(u: UserDict) -> str:
    return f"你好，{u['name']}，{u['age']} 岁"</code></pre>
    <p>
      JSON 读进来常常是 dict；不想上 dataclass 时，TypedDict 说明「应有哪些键、什么类型」。
      <strong>运行时仍是普通 dict</strong>，多键少键默认不报错，靠 mypy 等工具查。
    </p>

    <div class="callout callout--principle">
      <span class="callout__label">和 dataclass 怎么选</span>
      <p>
        要构造校验、方法、<code>asdict</code> → dataclass。
        只是描述「从 JSON 来的 dict 长什么样」→ TypedDict 更轻。
      </p>
    </div>

    <h2>Callable：函数当参数时的类型</h2>
    <p>
      <code>int</code>、<code>str</code> 好标；但参数<strong>本身是个函数</strong>时，
      只写 <code>f</code> 读的人不知道：要几个参数？什么类型？返回什么？
      <code>Callable</code> 就是给「可调用对象」写说明书。
    </p>

    <h3>语法：两层括号，别搞混</h3>
<pre><code>from typing import Callable

Callable[[参数类型1, 参数类型2, ...], 返回类型]</code></pre>
    <ul>
      <li>最外层 <code>Callable[...]</code>：这是一个「可调用」类型</li>
      <li>里面第一段 <code>[int, str]</code>：函数<strong>接收</strong>什么参数</li>
      <li>里面第二段 <code>bool</code>：函数<strong>返回</strong>什么</li>
    </ul>
    <p>常见几种读法：</p>
<pre><code>Callable[[int], int]        # 吃一个 int，吐一个 int
Callable[[], str]           # 无参数，返回 str
Callable[[int, int], bool]  # 吃两个 int，返回 bool</code></pre>

    <h3>配课例子拆开看</h3>
<pre><code>def apply_twice(f: Callable[[int], int], n: int) -> int:
    return f(f(n))

def inc(x: int) -> int:
    return x + 1

apply_twice(inc, 3)   # inc(3)=4 → inc(4)=5</code></pre>
    <p>
      <code>f</code> 必须是「接收 int、返回 int」的函数。
      <code>Callable[[int], int]</code> 写的就是这件事。
      若传 <code>greet(name: str) -&gt; str</code>，静态检查器会警告；运行时 Python 默认不拦。
    </p>

    <h3>和你已经学过的对上号</h3>
    <p>第 15 课 <code>sorted(scores, key=lambda x: x[1])</code>：</p>
<pre><code>scores = [("小明", 90), ("hulei", 75)]
sorted(scores, key=lambda x: x[1])</code></pre>
    <p>
      <code>key</code> 本质是「接收一个元素，返回用来比较的值」的函数。
      概念上可理解为 <code>Callable[[tuple[str, int]], int]</code>：
      吃 <code>(名字, 分数)</code>，吐 <code>int</code> 用于排序。
    </p>
    <p>
      第 23 课「函数是一等公民」：函数能当参数传、能被 return。
      <code>Callable</code> 只是给这种用法补上类型说明。
      接近 Java 的 <code>Function&lt;Integer, Integer&gt;</code>（概念类似，不是一一对应）。
    </p>

    <h3>更多写法</h3>
<pre><code>def combine(a: int, b: int, op: Callable[[int, int], int]) -> int:
    return op(a, b)

combine(3, 5, lambda x, y: x + y)   # 8
combine(3, 5, lambda x, y: x * y)   # 15

def repeat(action: Callable[[str], None], text: str, times: int) -> None:
    for _ in range(times):
        action(text)   # 无返回值的回调，返回类型写 None</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>Callable</code> 不会在运行时检查你传的函数对不对，也不会自动转换参数。
        它主要给读代码的人、IDE 补全、mypy/pyright 看。
        函数体里该写 <code>isinstance</code>、该处理异常，还是要自己写。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">怎么记</span>
      <p>
        <strong><code>Callable[[吃什么], 吐什么]</code></strong>：
        这里要传一个函数，这个函数的参数和返回值长这样。
        简单脚本不必强行写；高阶函数、策略/回调参数时再补即可。
      </p>
    </div>

    <h2>和 dataclass 一起用</h2>
<pre><code>from dataclasses import dataclass
from typing import Literal

@dataclass
class Task:
    title: str
    status: Literal["pending", "done"] = "pending"</code></pre>
    <p>字段类型、函数参数返回值可以混用；同一套 typing 词汇贯穿 dataclass 和普通函数。</p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>给成绩本的 <code>get_score</code> 补上 <code>-&gt; int | None</code>，调用处用 <code>is not None</code> 判断。</li>
      <li>写 <code>format_line(tag: int | str, msg: str) -&gt; str</code>，两种 tag 都能拼日志行。</li>
      <li>用 TypedDict 描述一条笔记 <code>{title, body}</code>，写函数取标题。</li>
      <li>做完配课 exercise 自检。</li>
    </ol>

    <h2>收束</h2>
    <p>
      带走一张小抄：<code>list[str]</code> 容器泛型、<code>T | None</code> 可能没有、
      <code>A | B</code> 多类型、<code>Literal</code> 固定值、<code>TypedDict</code> 字典结构、
      <code>Callable</code> 可调用类型。
      标注写清楚，三个月后的自己和队友都会感谢你。
      下一课可以学 <code>Enum</code>、<code>argparse</code>，或做 22～27 复习通关。
    </p>
  </div>
</template>
