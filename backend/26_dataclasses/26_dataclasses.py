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


# ---------- 3. 默认值 + field(default_factory=...) ----------
print("\n【3】默认值：可变类型必须用 default_factory")
# 错误示范（别这么写）：
#   tags: list[str] = []   ← 所有实例共用同一个 list！
# 正确：用 field(default_factory=list) 每次新建
@dataclass
class Article:
    title: str
    tags: list[str] = field(default_factory=list)

a1 = Article("Python 入门")
a2 = Article("装饰器")
a1.tags.append("基础")
print("  a1.tags =", a1.tags)    # ['基础']
print("  a2.tags =", a2.tags)    # []  没串


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
print("默认值放后面；list/dict 用 field(default_factory=...)")
print("frozen=True：不可变，能当 dict 键")
print("order=True：可比较、可 sorted；field(compare=False) 排除某字段")
print("__post_init__：构造后校验或算派生字段")
print("asdict/astuple：转 dict/元组，配合 json 很方便")
