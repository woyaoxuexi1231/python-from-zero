<template>
  <div class="article">
    <p>
      第 25 课第一次见 <code>collections</code>，和 <code>itertools</code> 挤在一起，
      很容易「看过命名、写题还是卡」。第 28 课<strong>只复习 collections</strong>，
      把 <code>defaultdict</code>、<code>Counter</code>、<code>namedtuple</code>、<code>deque</code>
      练到能随手用——不教新语法，专门补熟练度。
    </p>

    <h2>这一课解决什么问题</h2>
    <ul>
      <li>看见「按某键分组」→ 想到 <code>defaultdict(list)</code> / <code>defaultdict(set)</code></li>
      <li>看见「数出现几次、Top N」→ 想到 <code>Counter</code></li>
      <li>看见「几个字段绑一起、只读」→ 想到 <code>namedtuple</code></li>
      <li>看见「队列、最近 N 条、滑动窗口」→ 想到 <code>deque</code></li>
    </ul>

    <h2>defaultdict：三种工厂，别混</h2>
<pre><code>from collections import defaultdict

# 分组收集
by_key = defaultdict(list)
by_key["a"].append(1)

# 分组且去重
seen = defaultdict(set)
seen["u1"].add("/home")

# 计数（Counter 的内部思路类似）
hits = defaultdict(int)
for ch in "banana":
    hits[ch] += 1</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        缺键时不是 KeyError，而是调用你传的<strong>工厂函数</strong>造默认值：
        <code>list</code>、<code>set</code>、<code>int</code>（int() 得到 0）。
        等于把 <code>if key not in d: d[key] = []</code> 自动化了。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        写 <code>defaultdict(list())</code> 错——括号会立刻造一个 list 当工厂。
        正确是 <code>defaultdict(list)</code>。
        只想判断键在不在：用 <code>key in d</code>，别 <code>d[key]</code>，否则 defaultdict 会顺便创建键。
      </p>
    </div>

    <h2>Counter：专用计数，别手写排序</h2>
<pre><code>from collections import Counter

cnt = Counter("abracadabra")
cnt.most_common(2)          # [('a', 5), ('b', 2)]

a = Counter("aab")
b = Counter("abb")
a + b                        # 合并计数</code></pre>
    <p>
      和 <code>defaultdict(int)</code> 都能计数；要 <code>most_common</code>、要合并两个计数表，用 Counter 更省事。
    </p>

    <h2>defaultdict vs Counter：怎么选</h2>
    <table class="article-table">
      <thead>
        <tr>
          <th>需求</th>
          <th>用啥</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>每个键对应<strong>一列表</strong>或<strong>集合</strong></td>
          <td><code>defaultdict(list)</code> / <code>defaultdict(set)</code></td>
        </tr>
        <tr>
          <td>每个键<strong>出现几次</strong></td>
          <td><code>Counter</code> 或 <code>defaultdict(int)</code></td>
        </tr>
        <tr>
          <td>要 Top N 频次</td>
          <td><code>Counter.most_common(n)</code></td>
        </tr>
      </tbody>
    </table>

    <h2>namedtuple：轻量只读记录</h2>
<pre><code>from collections import namedtuple

Book = namedtuple("Book", ["title", "pages"])
b = Book("Python入门", 320)
b.title
b._replace(pages=400)   # 不可变，改字段返回新对象
b._asdict()             # 转 dict</code></pre>
    <p>字段少、不需要改、不用方法时合适；要可变和校验见第 26 课 dataclass。</p>

    <h2>deque：双端队列 + 滑动窗口（第 25 课没细讲）</h2>
<pre><code>from collections import deque

q = deque([1, 2, 3])
q.append(4)        # 右端加
q.appendleft(0)    # 左端加
q.pop()            # 右端出
q.popleft()        # 左端出

window = deque(maxlen=3)   # 最多保留 3 个，满了自动挤掉最左
for x in [1, 2, 3, 4, 5]:
    window.append(x)       # 滑动窗口</code></pre>
    <p>
      list 在头部 insert/pop 是 O(n)；deque 两头 O(1)。
      <code>maxlen=n</code> 常用来做「最近 N 条」或滚动平均。
    </p>

    <h2>collections 里还有哪些？（UserDict 等）</h2>
    <p>
      打开 <code>dir(collections)</code> 还会看到
      <code>UserDict</code>、<code>UserList</code>、<code>UserString</code>、
      <code>OrderedDict</code>、<code>ChainMap</code>、<code>abc</code> 等。
      第 28 课四个工具占日常九成；下面知道用途即可，不必背 API。
    </p>
    <table class="article-table">
      <thead>
        <tr>
          <th>名字</th>
          <th>干什么用</th>
          <th>日常要不要写</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>UserDict</code> / <code>UserList</code> / <code>UserString</code></td>
          <td>继承并<strong>改行为</strong>时的包装基类（内部持有一个真正的 dict/list/str）</td>
          <td>很少；要自定义映射/序列行为时才用</td>
        </tr>
        <tr>
          <td><code>OrderedDict</code></td>
          <td>保持插入顺序；另有 <code>move_to_end</code> 等（Py3.7+ 普通 dict 也有序）</td>
          <td>需要挪键顺序时用</td>
        </tr>
        <tr>
          <td><code>ChainMap</code></td>
          <td>多个 dict 叠成一层查找链，前面的键覆盖后面的（像局部配置覆盖默认配置）</td>
          <td>偶尔</td>
        </tr>
        <tr>
          <td><code>abc</code></td>
          <td><code>MutableMapping</code>、<code>Sequence</code> 等抽象基类，做接口约定 / <code>isinstance</code></td>
          <td>写框架、插件时可能见</td>
        </tr>
      </tbody>
    </table>
<pre><code>from collections import UserDict, OrderedDict, ChainMap

class UpperDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(str(key).upper(), value)

defaults = {"color": "red", "size": "M"}
merged = ChainMap({"color": "blue"}, defaults)
merged["color"]   # "blue" —— 前面的 dict 优先</code></pre>
    <div class="callout callout--pitfall">
      <span class="callout__label">易混</span>
      <p>
        第 27 课 <code>typing.TypedDict</code> 示例里有个 <code>class UserDict</code>——那是
        <strong>类型标注</strong>（描述 dict 有哪些键、什么类型），和
        <code>collections.UserDict</code>（可继承的 dict 包装类）<strong>完全不是一回事</strong>。
        只是碰巧都叫 UserDict，别混。
      </p>
    </div>
    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        内置 <code>dict</code> / <code>list</code> / <code>str</code> 在 C 里实现，直接
        <code>class MyDict(dict)</code> 子类化容易出奇怪 bug。
        <code>UserDict</code> 让你改 <code>__setitem__</code> 等方法，而不和 C 实现硬碰硬。
      </p>
    </div>

    <h2>为什么 collections 包只有一个 __init__.py？</h2>
    <p>
      用 Java 的眼光看标准库：<code>collections/</code> 目录里往往<strong>只有</strong>
      一个 <code>__init__.py</code>，Counter、deque 等全写在这一文件里——像「整个包只有一个源文件」，很反常。
    </p>
    <p>
      在 Python 里这<strong>完全合法</strong>，也不算坏实践：
    </p>
    <ul>
      <li>
        <strong>包</strong> = 文件夹 + <code>__init__.py</code>（Py3.3+ 命名空间包可以没有，但标准库 collections 是经典包）。
      </li>
      <li>
        Python <strong>不强制</strong>「一个类一个 .py」。小模块、稳定 API 全写进 <code>__init__.py</code> 很常见；
        <code>import collections</code> 时解释器执行这个文件，再把名字挂到模块上。
      </li>
      <li>
        标准库 <code>collections</code> 历史久、对外接口稳定，实现集中在一个大 <code>__init__.py</code> 里（几千行）——维护者熟悉，用户 <code>from collections import Counter</code> 也简单。
      </li>
    </ul>
    <p>
      <strong>和你自己项目的对照：</strong>Java 倾向 <code>com.example.User.java</code> 一文件一类；
      Python 倾向「按<strong>职责/体量</strong>拆文件」，不是按类数机械拆分。
    </p>
<pre><code># 项目变大时可以这样拆（示意）：
# collections_pkg/
#   __init__.py      ← from .counter import Counter; from .deque import deque
#   counter.py
#   deque.py

# 对外仍是：
from collections_pkg import Counter</code></pre>
    <div class="callout callout--principle">
      <span class="callout__label">结论</span>
      <p>
        不是「违反开发规范」，是两种语言不同的组织习惯。
        两三个类、几百行 → 单文件或单 <code>__init__.py</code> 没问题；
        目录膨胀、多人协作 → 拆成多个模块，<code>__init__.py</code> 只做统一出口（re-export）。
      </p>
    </div>

    <h2>配课怎么练</h2>
    <ol>
      <li>先跑 <code>28_collections_review.py</code>，对照输出理解四种工具。</li>
      <li>再打开 <code>28_collections_review_exercise.py</code>，6 题全是新场景。</li>
      <li>卡在某题：回知识文件「易错点」，别抄第 25 课答案。</li>
      <li>全绿后，自己用 Counter 统计一段中文或日志，用 defaultdict 分组试一遍。</li>
    </ol>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>用 <code>defaultdict(list)</code> 把同学名字按首字母分组。</li>
      <li>用 <code>Counter</code> 找一段文本里出现最多的 3 个词。</li>
      <li>用 <code>namedtuple</code> 解析 <code>"标题|页数"</code> 一行，<code>_replace</code> 加页数。</li>
      <li>用 <code>deque(maxlen=3)</code> 手算滚动平均，对照 exercise 题 5。</li>
    </ol>

    <h2>收束</h2>
    <p>
      collections 不是背 API，是四套固定套路：分组、计数、小对象、队列/窗口。
      熟练的标志是读题能选对工具，写题不混 defaultdict 和 Counter。
      下一课可以继续 typing 巩固、enum，或 itertools 单独复习——你哪块虚就补哪块。
    </p>
  </div>
</template>

<style scoped>
.article-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0 1.25rem;
  font-size: 0.92rem;
}

.article-table th,
.article-table td {
  border: 1px solid var(--border-subtle, rgba(0, 0, 0, 0.12));
  padding: 0.55rem 0.65rem;
  text-align: left;
}

.article-table th {
  background: var(--surface-muted, rgba(0, 0, 0, 0.04));
  font-weight: 600;
}
</style>
