# ============================================================
# 第 26 课（知识讲解）：dataclass —— 少写样板，专注数据
# 运行方式：python 26_dataclasses/26_dataclasses.py
# 配套练习：26_dataclasses_exercise.py（自检，全是新场景）
# ============================================================
from dataclasses import dataclass, field, asdict, astuple
from collections import namedtuple

# 痛点：一堆"只存数据"的类，手写 __init__ / __repr__ / __eq__ 很烦。
# 第 25 课 namedtuple 能起名字、能解包，但不能改字段、默认值写法也受限。
# dataclass 用 @dataclass 装饰器，帮你生成这些样板代码。
# 【Java 对照】≈ record（Java 16+）或 Lombok @Data
print("========== 第26课 dataclass ==========\n")


# ---------- 1. 最简 dataclass ----------
print("【1】@dataclass 自动生成 __init__ / __repr__ / __eq__")
@dataclass
class Point:
    x: int
    y: int

p = Point(3, 4)
print("  p =", p)                    # Point(x=3, y=4)
print("  p.x =", p.x)                # 3
print("  p == Point(3, 4) →", p == Point(3, 4))   # True


# ---------- 2. 对比：手写类 vs namedtuple vs dataclass ----------
print("\n【2】三种写法对照")
# 手写：字段一多就冗长
class PointManual:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"PointManual(x={self.x}, y={self.y})"

# namedtuple：不可变、轻量
Pt = namedtuple("Pt", ["x", "y"])
pt = Pt(1, 2)

# dataclass：可变（默认）、默认值友好、还能加方法
@dataclass
class Point2:
    x: int
    y: int = 0          # 有默认值的字段放后面

print("  手写:", PointManual(1, 2))
print("  namedtuple:", pt)
print("  dataclass 带默认:", Point2(5))   # Point2(x=5, y=0)


# ---------- 3. 默认值 + field(default_factory=...) —— 本课重点 ----------
print("\n【3】默认值：可变类型必须用 field(default_factory=...)")
print("  （第 13 课讲过函数默认参数；这里讲 dataclass 字段上的同一个坑）")

# ---- 3a. 回顾：第 13 课的函数默认值陷阱 ----
print("\n  【3a】回顾第 13 课：默认参数在「定义时」只求值一次")
# 错误写法（函数）：
#   def f(box=[]): ...     ← 所有调用共用同一个 list
# 正确写法（函数）：
#   def f(box=None):
#       if box is None: box = []

def add_item_wrong(item: str, box: list[str] = []) -> list[str]:
    box.append(item)
    return box

def add_item_ok(item: str, box: list[str] | None = None) -> list[str]:
    if box is None:
        box = []
    box.append(item)
    return box

print("    错误 f('a') →", add_item_wrong("a"))
print("    错误 f('b') →", add_item_wrong("b"), "← 两次调用串了！")
print("    正确 f('a') →", add_item_ok("a"))
print("    正确 f('b') →", add_item_ok("b"), "← 各自独立")

# ---- 3b. dataclass 字段上的 = [] 是同一个坑 ----
print("\n  【3b】dataclass 写 entries: list = [] 也一样危险")
print("    字段默认值在「类定义时」创建一次，不是每次 Gathering() 时创建。")
print("    Python 3.11+ 的 dataclass 会直接报错，不让你写 mutable default：")

try:
    @dataclass
    class GatheringWrong:
        entries: list[str] = []          # ❌ 现代 Python 定义类时就 ValueError
except ValueError as e:
    print("    ValueError:", e)
    print("    → 框架强制你用 default_factory，从语法层面堵住 = []")

# 用「手写 class + 默认 []」演示串数据（dataclass 已不让这么写，但原理相同）
class GatheringWrongManual:
    def __init__(self, entries: list[str] = []) -> None:
        self.entries = entries

g1 = GatheringWrongManual()
g2 = GatheringWrongManual()
g1.entries.append("张三报名")
print("    g1.entries =", g1.entries)
print("    g2.entries =", g2.entries, "← g2 没操作也有数据，串了！")

# ---- 3c. 不用 dataclass，手写 class 怎么规避？（第 13 课同款） ----
print("\n  【3c】手写 class 规避：默认 None，__init__ 里再新建 list")
class GatheringManual:
    def __init__(self, entries: list[str] | None = None) -> None:
        self.entries = [] if entries is None else entries

m1 = GatheringManual()
m2 = GatheringManual()
m1.entries.append("李四")
print("    m1.entries =", m1.entries)
print("    m2.entries =", m2.entries, "← 空列表，没串")

# ---- 3d. @dataclass 写 = [] 时，生成的 __init__ 大致长这样 ----
print("\n  【3d】若写 entries: list = []，dataclass 生成的大致等价代码：")
print("""
    _CLASS_DEFAULT_ENTRIES = []              # 类定义时创建，只此一份

    def __init__(self, entries=_CLASS_DEFAULT_ENTRIES):
        self.entries = entries               # 没传参 → 大家共用上面那个 list
""")
print("    这和手写 def __init__(self, entries=[]) 是同一个坑。")

# ---- 3e. 正确写法：field(default_factory=list) ----
print("\n  【3e】正确：field(default_factory=list)")
print("    default_factory 传「工厂函数」：每次需要默认值时调用 list() 新建空列表。")

@dataclass
class Article:
    title: str
    tags: list[str] = field(default_factory=list)

a1 = Article("Python 入门")
a2 = Article("装饰器")
a1.tags.append("基础")
print("    a1.tags =", a1.tags)    # ['基础']
print("    a2.tags =", a2.tags)    # []  没串

# ---- 3f. default_factory 时，dataclass 生成的 __init__ 大致长这样 ----
print("\n  【3f】field(default_factory=list) 时，生成的大致等价代码：")
print("""
    def __init__(self, entries=_MISSING):    # _MISSING 是 dataclass 内部哨兵
        if entries is _MISSING:
            self.entries = list()            # 每次实例化都调用 list()，新空列表
        else:
            self.entries = entries
""")
print("    关键：= [] 是类定义时建一次；default_factory 是每次 __init__ 且未传参时建。")

# ---- 3g. 为什么 int / str 可以直接写默认值？ ----
print("\n  【3g】对比：为什么 headcount = 1、note = '' 可以直接写？")
@dataclass
class EntryDemo:
    name: str
    headcount: int = 1       # 不可变，安全
    note: str = ""           # 不可变，安全

e1 = EntryDemo("小明")
e2 = EntryDemo("小红")
e1.headcount = 2           # 改的是 e1 自己的属性，不影响 e2
print("    e1.headcount =", e1.headcount, "  e2.headcount =", e2.headcount)
print("    int/str 改的是「赋值」，不会在原地改共享对象。")
print("    list 用 .append 改的是「对象本身」，共享就会串。")

# ---- 3h. 实战联系：family-gathering 项目的 Gathering.entries ----
print("\n  【3h】实战：family-gathering 里 Gathering.entries 就是这一写法")
print("    entries: list[Entry] = field(default_factory=list)")
print("    store.load() 文件不存在时会 Gathering()，必须每次得到独立空列表。")


# ---------- 4. frozen=True：不可变，可当 dict 的键 ----------
print("\n【4】frozen=True：冻结后不能改字段")
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

red = Color(255, 0, 0)
palette = {red: "红色"}
print("  palette[Color(255,0,0)] =", palette[Color(255, 0, 0)])
try:
    red.r = 100
except Exception as e:
    print("  改 frozen 字段 →", type(e).__name__)   # FrozenInstanceError


# ---------- 5. order=True：自动生成比较，方便排序 ----------
print("\n【5】order=True：按字段顺序比较 / sorted")
@dataclass(order=True)
class Student:
    score: int
    name: str = field(compare=False)   # 不参与比较，只比 score

students = [Student(85, "小明"), Student(92, "hulei"), Student(78, "小红")]
print("  按 score 排序:", sorted(students))


# ---------- 6. __post_init__：构造后校验 / 派生字段 ----------
print("\n【6】__post_init__：构造完再检查或补字段")
@dataclass
class Rect:
    width: int
    height: int
    area: int = field(init=False)      # init=False = 不进 __init__ 参数

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("宽和高必须为正")
        self.area = self.width * self.height

r = Rect(3, 4)
print("  Rect(3,4).area =", r.area)    # 12


# ---------- 7. asdict / astuple：转字典 / 元组（序列化常用） ----------
print("\n【7】asdict / astuple")
@dataclass
class User:
    name: str
    age: int

u = User("hulei", 18)
print("  asdict:", asdict(u))          # {'name': 'hulei', 'age': 18}
print("  astuple:", astuple(u))        # ('hulei', 18)


# ---------- 8. dataclass 里也能写方法 ----------
print("\n【8】dataclass 不是纯数据：可以加方法")
@dataclass
class Circle:
    radius: float

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

print("  Circle(2).area() ≈", round(Circle(2).area(), 2))


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("@dataclass：自动生成 __init__/__repr__/__eq__")
print("默认值放后面；list/dict/set 用 field(default_factory=...)")
print("  不能 = []：类定义时只求值一次，多实例共享（第13课函数默认值同一坑）")
print("  手写规避：def __init__(self, xs=None): self.xs = [] if xs is None else xs")
print("  dataclass 正确：default_factory=list → 每次 __init__ 调用 list() 新建")
print("frozen=True：不可变，能当 dict 键")
print("order=True：可比较、可 sorted；field(compare=False) 排除某字段")
print("__post_init__：构造后校验或算派生字段")
print("asdict/astuple：转 dict/元组，配合 json 很方便")
