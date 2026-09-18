# 第 26 课：dataclass 数据类

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门

**摘要**：@dataclass 少写样板、default_factory、frozen/order、__post_init__ 校验、asdict 序列化。

---

第 25 课 `namedtuple` 给元组起了字段名，但不可变、默认值写法受限。 `@dataclass` 是更现代的「数据类」：少写 `__init__` / `__repr__` / `__eq__`， 还能加默认值、校验、排序。接近 Java 的 `record` 或 Lombok `@Data`。

## 最简用法：让装饰器生成样板

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(3, 4)
print(p)                 # Point(x=3, y=4)
print(p == Point(3, 4))  # True
```

你只声明字段；装饰器根据注解自动生成构造、打印、相等比较。 精力放在「有哪些字段、字段什么意思」，而不是抄样板代码。

> **原理**
>
> `@dataclass` 是装饰器（第 23 课）：接收类，返回「补全了方法」的类。 运行时仍然是普通 class，没有魔法类型；只是省了你手写那几段固定代码。

## 默认值与 field：配方 vs 已经造好的东西

不可变默认值可以直接写：`y: int = 0`。 可变类型（list / dict / set）不行——默认值表达式在**定义类时只算一次**， 所有实例会共用同一个对象。

```python
# 错误：所有实例共用同一个 []
# tags: list[str] = []

from dataclasses import dataclass, field

@dataclass
class Article:
    title: str
    tags: list[str] = field(default_factory=list)
```

> **原理**
>
> Python 的默认值存的是「已经造好的对象」的引用，不是「每次新建的配方」。 所以 `= []` 只执行一次；`field(default_factory=list)` 才是配方——每次缺省时调用 `list()`，每个实例拿到新列表。 这和第 13 课「函数默认参数别用 `[]`」是同一类陷阱。

`field` 本身不是字段，而是**给字段写配置**的工具。常用参数：

- `default=...`：固定默认值（适合 int / str / None）
- `default_factory=list`：每次缺省时调用工厂造新值
- `init=False`：不进构造参数
- `compare=False`：不参与 `==` / 排序

> **踩坑**
>
> 写成 `field(default_factory=list())` 也不对—— 括号会立刻调用，传进去的是空列表，不是工厂函数。 正确是传 `list` 本身。

## frozen=True：不可变，能当 dict 的键

```python
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

palette = {Color(255, 0, 0): "红色"}
# palette[Color(255, 0, 0)] → "红色"
```

冻结后不能改字段；因为可哈希，可以放进 set、当 dict 键—— 语义接近 namedtuple 的不可变，但写法仍是 dataclass。

## order=True：排序与比较

```python
@dataclass(order=True)
class Student:
    score: int
    name: str = field(compare=False)   # 只比 score，不比 name

sorted([Student(85, "小明"), Student(92, "hulei"), Student(78, "小红")])
```

按字段声明顺序依次比较；用 `compare=False` 排除不想参与比较的字段。

## __post_init__：构造后校验或算派生字段

```python
@dataclass
class Rect:
    width: int
    height: int
    area: int = field(init=False)

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("宽和高必须为正")
        self.area = self.width * self.height
```

`__init__` 由 dataclass 自动生成； `__post_init__` 在它跑完之后执行。 适合「字段都赋好了，再检查合法性或补算 area」。 `field(init=False)` 表示该字段不进构造参数。

## asdict / astuple：转字典和元组

```python
from dataclasses import asdict, astuple

@dataclass
class User:
    name: str
    age: int

u = User("hulei", 18)
asdict(u)    # {'name': 'hulei', 'age': 18}
astuple(u)   # ('hulei', 18)
```

配合 `json.dump` 序列化时很常用；比手写字典转换省事。

## 和 namedtuple / 普通 class 怎么选

- **namedtuple**：轻量、不可变、字段少、不需要方法
- **dataclass**：需要默认值、可变、校验、方法、排序——日常首选
- **普通 class**：行为复杂、继承体系重、不只是「存数据」时用

## 建议你自己练的几件事

2. 写 frozen 坐标类，当 dict 键存棋盘颜色。
4. 写带 `default_factory` 的 Todo，验证两个实例的 tags 不会串。
6. 在 `__post_init__` 里校验邮箱必须含 `@`。
8. 用 `asdict` 把一批 User 转成 `list[dict]`；做完配课 exercise 自检。

## 收束

dataclass 让你把精力放在字段含义和业务逻辑，而不是重复写构造和比较。 记住一句就够：可变默认值用 `default_factory`，不要写 `= []`。 下一课 typing：把「可能没有、多种类型、固定几个值」写进类型标注。

---

上一课：[第 25 课：collections + itertools](25-collections + itertools.md)　|　下一课：[第 27 课：typing 类型标注进阶](27-typing 类型标注进阶.md)
