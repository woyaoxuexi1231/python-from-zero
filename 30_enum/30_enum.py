# ============================================================
# 第 30 课（知识讲解）：enum 枚举 —— 别再用魔法字符串
# 运行方式：python 30_enum/30_enum.py
# 配套练习：30_enum_exercise.py（自检，全是新场景）
# ============================================================
from enum import Enum, IntEnum, StrEnum, auto

# 痛点：状态写 "pending" / "done" 字符串，拼错运行时才炸，IDE 也不补全。
# enum 把「有限几个固定取值」收成一类，接近 Java 的 enum。
# 第 27 课 Literal["a","b"] 是类型标注；enum 是运行时真对象，能比较、能迭代。
print("========== 第30课 enum 枚举 ==========\n")


# ---------- 1. 基本 Enum：成员是唯一实例 ----------
print("【1】class Status(Enum)：每个成员是一个对象")
class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"

print("  Status.PENDING =", Status.PENDING)
print("  .name =", Status.PENDING.name)       # 成员名（代码里写的）
print("  .value =", Status.PENDING.value)     # 绑定的值
print("  是 Status 吗:", isinstance(Status.PENDING, Status))


# ---------- 2. 比较：同一枚举内用 is / ==，别和 str 混比 ----------
print("\n【2】比较与身份")
s = Status.PENDING
print("  s is Status.PENDING:", s is Status.PENDING)   # 单例，用 is 即可
print("  s == 'pending':", s == "pending")             # False！不是 str
print("  s.value == 'pending':", s.value == "pending") # 要比值就 .value
print("  Status.PENDING == Status.RUNNING:", Status.PENDING == Status.RUNNING)


# ---------- 3. 按 name / value 反查 ----------
print("\n【3】反查：Status['PENDING'] 与 Status('pending')")
print("  按名:", Status["PENDING"])
print("  按值:", Status("pending"))
print("  遍历:", [m.name for m in Status])


# ---------- 4. auto()：值自动递增（省得手写 1,2,3） ----------
print("\n【4】auto()：自动赋值")
class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

print("  Priority.LOW.value =", Priority.LOW.value)       # 1 起递增
print("  Priority.HIGH.value =", Priority.HIGH.value)


# ---------- 5. IntEnum：成员可以当 int 用 ----------
print("\n【5】IntEnum：和整数运算/比较")
class HttpCode(IntEnum):
    OK = 200
    NOT_FOUND = 404
    ERROR = 500

print("  HttpCode.OK == 200:", HttpCode.OK == 200)         # True
print("  HttpCode.OK + 1:", HttpCode.OK + 1)               # 201


# ---------- 6. StrEnum（Py3.11+）：成员就是 str ----------
print("\n【6】StrEnum：成员可当字符串用")
class Color(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

print("  Color.RED =", Color.RED)
print("  Color.RED == 'red':", Color.RED == "red")         # True
print("  拼接:", f"theme={Color.RED}")


# ---------- 7. 易错点 ----------
print("\n【7】易错点速记")
print("  ① 成员名必须大写是习惯，不是语法；但别和小写混用搞乱")
print("  ② Status.PENDING != 'pending'；要比字符串用 .value")
print("  ③ 不能继承已有成员再追加（Enum 限制）；要扩展用组合或 Flag")
print("  ④ JSON 序列化默认不能直接 dumps(Enum)；通常存 .value 或 .name")
print("  ⑤ Literal 是标注；Enum 是运行时类——写 API 边界时常一起用")


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("class X(Enum): A = 'a'  —— 固定取值集合")
print(".name / .value          —— 成员名 / 绑定值")
print("X['A'] / X('a')         —— 按名 / 按值反查")
print("auto()                  —— 自动 1,2,3…")
print("IntEnum / StrEnum       —— 当 int / 当 str 用")
print("和 Java enum 类似；别和魔法字符串混比")
