# 第 28 课：collections 复习强化

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门、复习

**摘要**：defaultdict 三种工厂、Counter 与 most_common、namedtuple、deque 滑动窗口；6 道新题练熟练。

---

第 25 课第一次见 `collections`，和 `itertools` 挤在一起， 很容易「看过命名、写题还是卡」。第 28 课**只复习 collections**， 把 `defaultdict`、`Counter`、`namedtuple`、`deque` 练到能随手用——不教新语法，专门补熟练度。

## 这一课解决什么问题

- 看见「按某键分组」→ 想到 `defaultdict(list)` / `defaultdict(set)`
- 看见「数出现几次、Top N」→ 想到 `Counter`
- 看见「几个字段绑一起、只读」→ 想到 `namedtuple`
- 看见「队列、最近 N 条、滑动窗口」→ 想到 `deque`

## defaultdict：三种工厂，别混

```python
from collections import defaultdict

# 分组收集
by_key = defaultdict(list)
by_key["a"].append(1)

# 分组且去重
seen = defaultdict(set)
seen["u1"].add("/home")

# 计数（Counter 的内部思路类似）
hits = defaultdict(int)
for ch in "banana":
    hits[ch] += 1
```

> **原理**
>
> 缺键时不是 KeyError，而是调用你传的**工厂函数**造默认值： `list`、`set`、`int`（int() 得到 0）。 等于把 `if key not in d: d[key] = []` 自动化了。

> **踩坑**
>
> 写 `defaultdict(list())` 错——括号会立刻造一个 list 当工厂。 正确是 `defaultdict(list)`。 只想判断键在不在：用 `key in d`，别 `d[key]`，否则 defaultdict 会顺便创建键。

## Counter：专用计数，别手写排序

```python
from collections import Counter

cnt = Counter("abracadabra")
cnt.most_common(2)          # [('a', 5), ('b', 2)]

a = Counter("aab")
b = Counter("abb")
a + b                        # 合并计数
```

和 `defaultdict(int)` 都能计数；要 `most_common`、要合并两个计数表，用 Counter 更省事。

## defaultdict vs Counter：怎么选

| 需求 | 用啥 |
| --- | --- |
| 每个键对应**一列表**或**集合** | `defaultdict(list)` / `defaultdict(set)` |
| 每个键**出现几次** | `Counter` 或 `defaultdict(int)` |
| 要 Top N 频次 | `Counter.most_common(n)` |

## namedtuple：轻量只读记录

```python
from collections import namedtuple

Book = namedtuple("Book", ["title", "pages"])
b = Book("Python入门", 320)
b.title
b._replace(pages=400)   # 不可变，改字段返回新对象
b._asdict()             # 转 dict
```

字段少、不需要改、不用方法时合适；要可变和校验见第 26 课 dataclass。

## deque：双端队列 + 滑动窗口（第 25 课没细讲）

```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)        # 右端加
q.appendleft(0)    # 左端加
q.pop()            # 右端出
q.popleft()        # 左端出

window = deque(maxlen=3)   # 最多保留 3 个，满了自动挤掉最左
for x in [1, 2, 3, 4, 5]:
    window.append(x)       # 滑动窗口
```

list 在头部 insert/pop 是 O(n)；deque 两头 O(1)。 `maxlen=n` 常用来做「最近 N 条」或滚动平均。

## collections 里还有哪些？（UserDict 等）

打开 `dir(collections)` 还会看到 `UserDict`、`UserList`、`UserString`、 `OrderedDict`、`ChainMap`、`abc` 等。 第 28 课四个工具占日常九成；下面知道用途即可，不必背 API。

| 名字 | 干什么用 | 日常要不要写 |
| --- | --- | --- |
| `UserDict` / `UserList` / `UserString` | 继承并**改行为**时的包装基类（内部持有一个真正的 dict/list/str） | 很少；要自定义映射/序列行为时才用 |
| `OrderedDict` | 保持插入顺序；另有 `move_to_end` 等（Py3.7+ 普通 dict 也有序） | 需要挪键顺序时用 |
| `ChainMap` | 多个 dict 叠成一层查找链，前面的键覆盖后面的（像局部配置覆盖默认配置） | 偶尔 |
| `abc` | `MutableMapping`、`Sequence` 等抽象基类，做接口约定 / `isinstance` | 写框架、插件时可能见 |

```python
from collections import UserDict, OrderedDict, ChainMap

class UpperDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(str(key).upper(), value)

defaults = {"color": "red", "size": "M"}
merged = ChainMap({"color": "blue"}, defaults)
merged["color"]   # "blue" —— 前面的 dict 优先
```

> **易混**
>
> 第 27 课 `typing.TypedDict` 示例里有个 `class UserDict`——那是 **类型标注**（描述 dict 有哪些键、什么类型），和 `collections.UserDict`（可继承的 dict 包装类）**完全不是一回事**。 只是碰巧都叫 UserDict，别混。

> **原理**
>
> 内置 `dict` / `list` / `str` 在 C 里实现，直接 `class MyDict(dict)` 子类化容易出奇怪 bug。 `UserDict` 让你改 `__setitem__` 等方法，而不和 C 实现硬碰硬。

## 为什么 collections 包只有一个 __init__.py？

用 Java 的眼光看标准库：`collections/` 目录里往往**只有** 一个 `__init__.py`，Counter、deque 等全写在这一文件里——像「整个包只有一个源文件」，很反常。

在 Python 里这**完全合法**，也不算坏实践：

- **包** = 文件夹 + `__init__.py`（Py3.3+ 命名空间包可以没有，但标准库 collections 是经典包）。
- Python **不强制**「一个类一个 .py」。小模块、稳定 API 全写进 `__init__.py` 很常见； `import collections` 时解释器执行这个文件，再把名字挂到模块上。
- 标准库 `collections` 历史久、对外接口稳定，实现集中在一个大 `__init__.py` 里（几千行）——维护者熟悉，用户 `from collections import Counter` 也简单。

**和你自己项目的对照：**Java 倾向 `com.example.User.java` 一文件一类； Python 倾向「按**职责/体量**拆文件」，不是按类数机械拆分。

```python
# 项目变大时可以这样拆（示意）：
# collections_pkg/
#   __init__.py      ← from .counter import Counter; from .deque import deque
#   counter.py
#   deque.py

# 对外仍是：
from collections_pkg import Counter
```

> **结论**
>
> 不是「违反开发规范」，是两种语言不同的组织习惯。 两三个类、几百行 → 单文件或单 `__init__.py` 没问题； 目录膨胀、多人协作 → 拆成多个模块，`__init__.py` 只做统一出口（re-export）。

## 配课怎么练

2. 先跑 `28_collections_review.py`，对照输出理解四种工具。
4. 再打开 `28_collections_review_exercise.py`，6 题全是新场景。
6. 卡在某题：回知识文件「易错点」，别抄第 25 课答案。
8. 全绿后，自己用 Counter 统计一段中文或日志，用 defaultdict 分组试一遍。

## 建议你自己练的几件事

2. 用 `defaultdict(list)` 把同学名字按首字母分组。
4. 用 `Counter` 找一段文本里出现最多的 3 个词。
6. 用 `namedtuple` 解析 `"标题|页数"` 一行，`_replace` 加页数。
8. 用 `deque(maxlen=3)` 手算滚动平均，对照 exercise 题 5。

## 收束

collections 不是背 API，是四套固定套路：分组、计数、小对象、队列/窗口。 熟练的标志是读题能选对工具，写题不混 defaultdict 和 Counter。 下一课可以继续 typing 巩固、enum，或 itertools 单独复习——你哪块虚就补哪块。

---

上一课：[第 27 课：typing 类型标注进阶](27-typing 类型标注进阶.md)　|　下一课：[第 29 课：itertools 复习强化](29-itertools 复习强化.md)
