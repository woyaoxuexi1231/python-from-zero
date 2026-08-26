# ============================================================
# 第 26 课（练习）：dataclass —— 全部是新场景
# 运行方式：python 26_dataclasses/26_dataclasses_exercise.py
# ============================================================
from dataclasses import dataclass, field, asdict

# 先读 26_dataclasses.py 学 @dataclass / field / frozen / order / __post_init__。
# 下面 5 个是新场景：把 dataclass 用到别的地方去。写完自检 ✅/❌。

# ---------- 题 1：Book 数据类 + 统计总页数 ----------
# 场景：图书馆要统计一批书的总页数。
# 写 @dataclass Book，字段 title(str) 和 pages(int)。
# 再写 total_pages(books)：返回所有 Book 的 pages 之和。
#   提示：sum(b.pages for b in books)
@dataclass
class Book:
    pass   # 填字段


def total_pages(books: list) -> int:
    pass   # 填


# ---------- 题 2：frozen 坐标当 dict 键 ----------
# 场景：棋盘上的棋子位置 (x,y) 要当字典键查颜色。
# 写 @dataclass(frozen=True) Pos，字段 x(int)、y(int)。
# 再写 lookup(board, pos)：board 是 dict[Pos, str]，返回 pos 对应颜色；
#   若 pos 不在 board，返回 "空"。
#   提示：board.get(pos, "空")
@dataclass(frozen=True)
class Pos:
    pass   # 填字段


def lookup(board: dict, pos) -> str:
    pass   # 填


# ---------- 题 3：Todo 的 tags 用 default_factory ----------
# 场景：待办事项，每条可以挂多个标签；新建时 tags 默认空列表。
# 写 @dataclass Todo：title(str)，tags(list[str]) 默认空。
#   必须用 field(default_factory=list)，不能写 = []。
# 再写 add_tag(todo, tag)：往 todo.tags 追加 tag，返回 todo 本身（方便链式）。
@dataclass
class Todo:
    pass   # 填字段


def add_tag(todo, tag: str):
    pass   # 填


# ---------- 题 4：Email 构造后校验 ----------
# 场景：用户邮箱必须含 @，否则构造时就报错。
# 写 @dataclass Email，字段 address(str)。
#   在 __post_init__ 里：若 "@" not in self.address，raise ValueError("无效邮箱")。
@dataclass
class Email:
    pass   # 填字段 + __post_init__


# ---------- 题 5：批量转 dict（asdict） ----------
# 场景：要把一批用户对象序列化成 JSON 友好的 list[dict]。
# 写 @dataclass User：name(str)、age(int)。
# 再写 users_to_dicts(users)：用 asdict 把每个 User 转成 dict，返回 list。
@dataclass
class User:
    pass   # 填字段


def users_to_dicts(users: list) -> list[dict]:
    pass   # 填


# ============ 测试框架（不用改）============
def run_tests(title: str, cases: list[tuple]) -> bool:
    print(f"\n===== {title} =====")
    ok = 0
    for i, (expected, actual, desc) in enumerate(cases, 1):
        passed = expected == actual
        ok += passed
        mark = "✅" if passed else "❌"
        print(f"  {mark} 用例{i:02d} {desc}")
        if not passed:
            print(f"        期望: {expected!r}")
            print(f"        实际: {actual!r}")
    total = len(cases)
    print(f"  ---> {title}: {ok}/{total} 通过")
    return ok == total


def raises(fn, exc=Exception):
    try:
        fn()
    except exc:
        return True
    except Exception:
        return False
    return False


if __name__ == "__main__":
    all_pass = True

    # ---- 题1：总页数 ----
    books = [Book("Python", 300), Book("算法", 500), Book("随笔", 120)]
    all_pass &= run_tests("题1 total_pages", [
        (total_pages(books), 920, "三本书页数之和"),
        (total_pages([]), 0, "空列表为 0"),
    ])

    # ---- 题2：frozen 坐标查色 ----
    board = {Pos(0, 0): "白", Pos(1, 1): "黑"}
    all_pass &= run_tests("题2 lookup(frozen Pos)", [
        (lookup(board, Pos(0, 0)), "白", "存在的键"),
        (lookup(board, Pos(2, 2)), "空", "不存在的键"),
    ])

    # ---- 题3：tags 不串 + add_tag ----
    t1 = Todo("学 dataclass")
    t2 = Todo("写练习")
    add_tag(t1, "python")
    add_tag(t1, "基础")
    add_tag(t2, "作业")
    all_pass &= run_tests("题3 Todo default_factory", [
        (t1.tags, ["python", "基础"], "t1 两个标签"),
        (t2.tags, ["作业"], "t2 独立，没被 t1 污染"),
    ])

    # ---- 题4：邮箱校验 ----
    good = Email("a@b.com")
    all_pass &= run_tests("题4 Email __post_init__", [
        (good.address, "a@b.com", "合法邮箱能构造"),
        (raises(lambda: Email("invalid"), ValueError), True, "无 @ 抛 ValueError"),
    ])

    # ---- 题5：asdict 批量 ----
    users = [User("小明", 18), User("hulei", 20)]
    all_pass &= run_tests("题5 users_to_dicts", [
        (users_to_dicts(users),
         [{"name": "小明", "age": 18}, {"name": "hulei", "age": 20}],
         "每个 User 变成 dict"),
        (users_to_dicts([]), [], "空列表"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！dataclass 从定义到校验到序列化都会用了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")
