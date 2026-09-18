# 第 27 课：typing 类型标注进阶

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门

**摘要**：list[str]/dict[K,V]、Optional 与 | None、Union、Literal、TypedDict、Callable、与 dataclass 联用。

---

第 1 课学过 `a: int`、`-> str`；第 26 课 dataclass 字段也在写类型。 这一课补日常最常见的几种：**可能没有**、**多种类型之一**、 **只能是固定几个值**、**字典的结构说明**。 接近 Java 的泛型、`Optional`、枚举字面量——但 Python 标注默认**不拦运行时**，主要给编辑器和检查工具看。

## 先记住：标注是说明书，不是运行时警察

```python
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)       # 3
add("1", "2")   # "12" —— 运行时照样跑，不会 TypeError
```

> **原理**
>
> 类型标注主要服务 IDE 补全、mypy、pyright 等静态检查。 想「查错」要额外跑检查器；不能指望 CPython 因为标注不符就拒绝执行。 这和 Java 编译期强制类型不同——Python 仍是动态语言，标注是可选的文档层。

## 容器泛型：list[str]、dict[str, int]

```python
names: list[str] = ["小明", "hulei"]
scores: dict[str, int] = {"小明": 90}
pair: tuple[int, str] = (1, "A")
many: tuple[int, ...] = (1, 2, 3)   # 长度不定，元素都是 int

def top_scorer(book: dict[str, int]) -> str:
    return max(book, key=book.get)
```

不只标「是 list」，还要标「装什么」。读代码的人一眼知道： `book` 是「名字 → 分数」，返回值是某个名字（str）。

## T | None / Optional[T]：可能没有

第 12 课 `get_score` 找不到人返回 `None`，标注应写清楚。

```python
def find_score(book: dict[str, int], name: str) -> int | None:
    return book.get(name)

# 旧写法，等价：
# from typing import Optional
# def find_score(...) -> Optional[int]: ...
```

调用方看到 `| None`，就知道要先判断： `if (s := find_score(book, name)) is not None:` 再用。

> **踩坑**
>
> 写了 `-> int` 却可能返回 `None`，编辑器不会帮你 runtime 报错， 但静态检查会警告——这是标注的价值：把「可能没有」写进签名，别藏惊喜。

## A | B / Union：多种类型之一

```python
def double_value(x: int | str) -> int | str:
    if isinstance(x, int):
        return x * 2
    return x + x
```

参数或返回值可以是几种类型之一。Python 3.10+ 推荐 `int | str`； 旧代码常见 `Union[int, str]`，含义相同。 运行时仍要靠 `isinstance` 分支处理，标注不会自动帮你转换。

## Literal：只能是几个固定值

```python
from typing import Literal

Status = Literal["pending", "done", "cancelled"]

def set_status(task_id: int, status: Status) -> str:
    return f"任务 {task_id} → {status}"
```

比 `str` 更窄：只能是 `"pending"`、`"done"`、`"cancelled"` 之一。 编辑器会提示合法值；传 `"running"` 静态检查会警告。 接近「字符串版枚举」，但仍是 str，不是 Enum 类。

## TypedDict：给 dict 定字段表

```python
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int

def greet_user(u: UserDict) -> str:
    return f"你好，{u['name']}，{u['age']} 岁"
```

JSON 读进来常常是 dict；不想上 dataclass 时，TypedDict 说明「应有哪些键、什么类型」。 **运行时仍是普通 dict**，多键少键默认不报错，靠 mypy 等工具查。

> **和 dataclass 怎么选**
>
> 要构造校验、方法、`asdict` → dataclass。 只是描述「从 JSON 来的 dict 长什么样」→ TypedDict 更轻。

## Callable：函数当参数时的类型

`int`、`str` 好标；但参数**本身是个函数**时， 只写 `f` 读的人不知道：要几个参数？什么类型？返回什么？ `Callable` 就是给「可调用对象」写说明书。

### 语法：两层括号，别搞混

```python
from typing import Callable

Callable[[参数类型1, 参数类型2, ...], 返回类型]
```

- 最外层 `Callable[...]`：这是一个「可调用」类型
- 里面第一段 `[int, str]`：函数**接收**什么参数
- 里面第二段 `bool`：函数**返回**什么

常见几种读法：

```python
Callable[[int], int]        # 吃一个 int，吐一个 int
Callable[[], str]           # 无参数，返回 str
Callable[[int, int], bool]  # 吃两个 int，返回 bool
```

### 配课例子拆开看

```python
def apply_twice(f: Callable[[int], int], n: int) -> int:
    return f(f(n))

def inc(x: int) -> int:
    return x + 1

apply_twice(inc, 3)   # inc(3)=4 → inc(4)=5
```

`f` 必须是「接收 int、返回 int」的函数。 `Callable[[int], int]` 写的就是这件事。 若传 `greet(name: str) -> str`，静态检查器会警告；运行时 Python 默认不拦。

### 和你已经学过的对上号

第 15 课 `sorted(scores, key=lambda x: x[1])`：

```python
scores = [("小明", 90), ("hulei", 75)]
sorted(scores, key=lambda x: x[1])
```

`key` 本质是「接收一个元素，返回用来比较的值」的函数。 概念上可理解为 `Callable[[tuple[str, int]], int]`： 吃 `(名字, 分数)`，吐 `int` 用于排序。

第 23 课「函数是一等公民」：函数能当参数传、能被 return。 `Callable` 只是给这种用法补上类型说明。 接近 Java 的 `Function<Integer, Integer>`（概念类似，不是一一对应）。

### 更多写法

```python
def combine(a: int, b: int, op: Callable[[int, int], int]) -> int:
    return op(a, b)

combine(3, 5, lambda x, y: x + y)   # 8
combine(3, 5, lambda x, y: x * y)   # 15

def repeat(action: Callable[[str], None], text: str, times: int) -> None:
    for _ in range(times):
        action(text)   # 无返回值的回调，返回类型写 None
```

> **原理**
>
> `Callable` 不会在运行时检查你传的函数对不对，也不会自动转换参数。 它主要给读代码的人、IDE 补全、mypy/pyright 看。 函数体里该写 `isinstance`、该处理异常，还是要自己写。

> **怎么记**
>
> **`Callable[[吃什么], 吐什么]`**： 这里要传一个函数，这个函数的参数和返回值长这样。 简单脚本不必强行写；高阶函数、策略/回调参数时再补即可。

## 和 dataclass 一起用

```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class Task:
    title: str
    status: Literal["pending", "done"] = "pending"
```

字段类型、函数参数返回值可以混用；同一套 typing 词汇贯穿 dataclass 和普通函数。

## 建议你自己练的几件事

2. 给成绩本的 `get_score` 补上 `-> int | None`，调用处用 `is not None` 判断。
4. 写 `format_line(tag: int | str, msg: str) -> str`，两种 tag 都能拼日志行。
6. 用 TypedDict 描述一条笔记 `{title, body}`，写函数取标题。
8. 做完配课 exercise 自检。

## 收束

带走一张小抄：`list[str]` 容器泛型、`T | None` 可能没有、 `A | B` 多类型、`Literal` 固定值、`TypedDict` 字典结构、 `Callable` 可调用类型。 标注写清楚，三个月后的自己和队友都会感谢你。 下一课可以学 `Enum`、`argparse`，或做 22～27 复习通关。

---

上一课：[第 26 课：dataclass 数据类](26-dataclass 数据类.md)　|　下一课：[第 28 课：collections 复习强化](28-collections 复习强化.md)
