# ============================================================
# 第 27 课（练习）：typing 类型标注进阶 —— 全部是新场景
# 运行方式：python 27_typing/27_typing_exercise.py
# ============================================================
from typing import Literal, TypedDict

# 先读 27_typing.py。标注主要给编辑器和 mypy 看；下面 5 题练「把类型写对」。
# 实现函数逻辑即可；类型注解按题目要求写上。

# ---------- 题 1：可能找不到 → 返回 int | None ----------
# 场景：商品表 dict[商品名, 价格]，查不到时返回 None（不要抛 KeyError）。
# 写 price_of(catalog, name) -> int | None。
#   提示：catalog.get(name)
def price_of(catalog: dict[str, int], name: str) -> int | None:
    pass   # 填


# ---------- 题 2：参数可以是 int 或 str，统一成 str ----------
# 场景：日志行前缀有时传数字有时传文字，最终都要变成 str 拼进一行。
# 写 format_line(tag, msg) -> str：
#   tag 类型标注为 int | str；msg 为 str。
#   若 tag 是 int，先 str(tag)；若是 str 直接用。
#   返回 f"[{tag}] {msg}"（tag 已是 str）。
def format_line(tag: int | str, msg: str) -> str:
    pass   # 填


# ---------- 题 3：Literal 限制状态值 ----------
# 场景：订单只有三种状态。
OrderStatus = Literal["created", "paid", "shipped"]

def describe_order(order_id: int, status: OrderStatus) -> str:
    pass   # 填：返回 f"订单{order_id}:{status}"


# ---------- 题 4：TypedDict 描述一条笔记 ----------
# 场景：JSON 读进来的笔记是 dict，但字段固定为 title / body。
class NoteDict(TypedDict):
    pass   # 填字段 title: str, body: str

def note_title(note: NoteDict) -> str:
    pass   # 填：返回 note["title"]


# ---------- 题 5：list[某类型] 聚合 ----------
# 场景：一批 NoteDict，拼出所有标题的 list[str]。
def all_titles(notes: list[NoteDict]) -> list[str]:
    pass   # 填：列表推导 [n["title"] for n in notes]


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


if __name__ == "__main__":
    all_pass = True

    catalog = {"苹果": 5, "香蕉": 3}

    all_pass &= run_tests("题1 price_of", [
        (price_of(catalog, "苹果"), 5, "存在"),
        (price_of(catalog, "西瓜"), None, "不存在返回 None"),
    ])

    all_pass &= run_tests("题2 format_line", [
        (format_line(404, "未找到"), "[404] 未找到", "tag 是 int"),
        (format_line("INFO", "启动"), "[INFO] 启动", "tag 是 str"),
    ])

    all_pass &= run_tests("题3 describe_order", [
        (describe_order(1001, "paid"), "订单1001:paid", "Literal 状态"),
        (describe_order(2, "shipped"), "订单2:shipped", "另一种状态"),
    ])

    n1: NoteDict = {"title": "Python", "body": "typing"}
    n2: NoteDict = {"title": "Java", "body": "generics"}
    all_pass &= run_tests("题4 note_title", [
        (note_title(n1), "Python", "取 title"),
    ])

    all_pass &= run_tests("题5 all_titles", [
        (all_titles([n1, n2]), ["Python", "Java"], "批量标题"),
        (all_titles([]), [], "空列表"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！Optional/Union/Literal/TypedDict 都会写了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")
