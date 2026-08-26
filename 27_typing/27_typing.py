# ============================================================
# 第 27 课（知识讲解）：typing 类型标注进阶
# 运行方式：python 27_typing/27_typing.py
# 配套练习：27_typing_exercise.py（自检，全是新场景）
# ============================================================
from typing import Optional, Union, Literal, TypedDict, Callable
from dataclasses import dataclass

# 痛点：函数参数/返回值一多，光看名字猜不出「该传什么、会返回什么」。
# 第 1 课学过 a: int -> int；这一课补「可能没有」「多种类型」「固定几个值」等日常写法。
# 【Java 对照】
#   Optional[T]     ≈ Optional<T>
#   Union[A, B]     ≈ A | B（Java 14+）
#   Literal["a","b"] ≈ 枚举字面量 / sealed 的一种轻量写法
#   TypedDict       ≈ 没有 class 的 Map<String, Object> 结构说明
#
# 重要：标注主要给编辑器和类型检查器（mypy/pyright）看；
#       CPython 默认不会因为类型不对就拒绝运行（除非你用额外工具检查）。
print("========== 第27课 typing 类型标注进阶 ==========\n")


# ---------- 1. 复习：标注是「说明书」，不是运行时警察 ----------
print("【1】标注写给人和工具看，默认不拦你乱传")
def add(a: int, b: int) -> int:
    return a + b

print("  add(1, 2) =", add(1, 2))
print("  add('1', '2') =", add("1", "2"))   # 运行时照样跑，结果是 '12'
print("  → 想强制检查：用 mypy / pyright，不是指望 Python 自己拦")


# ---------- 2. 容器泛型：list[str]、dict[str, int] ----------
print("\n【2】容器也要写「装什么」")
names: list[str] = ["小明", "hulei"]
scores: dict[str, int] = {"小明": 90, "hulei": 75}
pair: tuple[int, str] = (1, "A")          # 固定长度、各位置类型
many: tuple[int, ...] = (1, 2, 3)         # 长度不定，元素都是 int

def top_scorer(book: dict[str, int]) -> str:
    return max(book, key=book.get)

print("  最高分:", top_scorer(scores))


# ---------- 3. Optional / X | None：可能没有 ----------
print("\n【3】Optional[T] 与 T | None：返回值「有或没有」")
# 第 12 课 get_score 找不到人返回 None，标注应写清楚。

def find_score(book: dict[str, int], name: str) -> int | None:
    return book.get(name)                   # 有就 int，没有 None

def find_score_old(book: dict[str, int], name: str) -> Optional[int]:
    return book.get(name)                   # 同上，旧写法，等价

print("  存在:", find_score(scores, "小明"))
print("  不存在:", find_score(scores, "不存在"))
# 调用方应写：if (s := find_score(...)) is not None: ...


# ---------- 4. Union / X | Y：多种类型之一 ----------
print("\n【4】Union 与 X | Y：参数可以是几种类型之一")
def double_value(x: int | str) -> int | str:
    if isinstance(x, int):
        return x * 2
    return x + x                            # str 拼接两份

print("  double_value(3) =", double_value(3))
print("  double_value('hi') =", double_value("hi"))

# Union[int, str] 与 int | str 等价（3.10+ 推荐用 |）


# ---------- 5. Literal：只能是几个固定值 ----------
print("\n【5】Literal：值必须是字面量集合里的某一个")
Status = Literal["pending", "done", "cancelled"]

def set_status(task_id: int, status: Status) -> str:
    return f"任务 {task_id} → {status}"

print(" ", set_status(1, "done"))
# set_status(1, "running")  # 编辑器/mypy 会警告；运行时 Python 不拦


# ---------- 6. TypedDict：给 dict 定字段结构 ----------
print("\n【6】TypedDict：字典也有「字段表」")
class UserDict(TypedDict):
    name: str
    age: int

def greet_user(u: UserDict) -> str:
    return f"你好，{u['name']}，{u['age']} 岁"

u: UserDict = {"name": "hulei", "age": 18}
print(" ", greet_user(u))
# TypedDict 运行时仍是普通 dict；多/少键默认不报错，靠类型检查器抓


# ---------- 7. Callable：「可调用」的类型 ----------
print("\n【7】Callable[[参数类型...], 返回类型]")
def apply_twice(f: Callable[[int], int], n: int) -> int:
    return f(f(n))

def inc(x: int) -> int:
    return x + 1

print("  apply_twice(inc, 3) =", apply_twice(inc, 3))   # inc(inc(3)) = 5


# ---------- 8. 和 dataclass 一起用 ----------
print("\n【8】dataclass 字段 + 函数返回值一起标注")
@dataclass
class Task:
    title: str
    status: Literal["pending", "done"] = "pending"

def mark_done(t: Task) -> Task:
    t.status = "done"
    return t

t = Task("写报告")
print("  完成前:", t)
print("  完成后:", mark_done(t))


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("list[str] / dict[K,V] / tuple[int,...]：容器里装什么")
print("T | None / Optional[T]：可能没有")
print("A | B / Union[A,B]：多种类型之一")
print("Literal['a','b']：只能是这几个固定值")
print("TypedDict：dict 的结构说明（运行时仍是 dict）")
print("Callable[[Arg], Ret]：函数当参数时的类型")
print("标注默认不强制；要查错用 mypy / pyright")
