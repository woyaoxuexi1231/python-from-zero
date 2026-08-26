# ============================================================
# 第 29 课（练习）：itertools 复习强化 —— 全部是新场景
# 运行方式：python 29_itertools_review/29_itertools_review_exercise.py
# ============================================================
import itertools

# 先读 29_itertools_review.py，把工具再跑一遍。
# 下面 6 题只考 itertools，场景都是新的。写完自检 ✅/❌。
# 卡住时：回知识文件看「小抄」和易错点，不要抄第 25 课 exercise 答案。

# ---------- 题 1：chain.from_iterable 展平 ----------
# 写 flatten(nested: list[list[_T]]) -> list
#   把二维 list 压成一维，保序。
#   例：[[1,2],[3],[]] → [1,2,3]
def flatten(nested: list) -> list:
    pass


# ---------- 题 2：islice 从 count 取一段 ----------
# 写 first_n(start: int, n: int) -> list[int]
#   返回从 start 开始的 n 个连续整数（含 start）。
#   例：first_n(10, 5) → [10, 11, 12, 13, 14]
def first_n(start: int, n: int) -> list:
    pass


# ---------- 题 3：sort + groupby 按字段分组 ----------
# 写 group_by_class(students: list[tuple[str, str]]) -> dict[str, list[str]]
#   students 每项是 (姓名, 班级)。返回 {班级: [姓名…]}，姓名顺序与输入一致。
#   提示：先按班级 sort，再 groupby(key=…)，组内顺序保持 sort 稳定后的顺序。
def group_by_class(students: list[tuple[str, str]]) -> dict:
    pass


# ---------- 题 4：combinations 两两配对 ----------
# 写 all_pairs(items: list) -> list[tuple]
#   返回 items 中任意 2 个的不同组合（无序），顺序与 combinations 一致。
#   例：all_pairs(["A","B","C"]) → [("A","B"),("A","C"),("B","C")]
def all_pairs(items: list) -> list:
    pass


# ---------- 题 5：accumulate 前缀和 ----------
# 写 prefix_sums(nums: list[int]) -> list[int]
#   返回前缀和列表。例：[1,2,3,4] → [1,3,6,10]
def prefix_sums(nums: list[int]) -> list:
    pass


# ---------- 题 6：综合 —— product 生成套餐组合 ----------
# 写 meal_combos(mains: list[str], drinks: list[str]) -> list[tuple[str, str]]
#   返回 (主菜, 饮料) 的笛卡尔积，顺序与 itertools.product(mains, drinks) 一致。
def meal_combos(mains: list[str], drinks: list[str]) -> list:
    pass


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

    all_pass &= run_tests("题1 flatten", [
        (flatten([[1, 2], [3], []]), [1, 2, 3], "展平二维"),
        (flatten([[]]), [], "全空"),
    ])

    all_pass &= run_tests("题2 first_n", [
        (first_n(10, 5), [10, 11, 12, 13, 14], "从10取5个"),
        (first_n(0, 3), [0, 1, 2], "从0取3个"),
    ])

    students = [("Bob", "A"), ("Amy", "B"), ("Anna", "A"), ("Cara", "B")]
    all_pass &= run_tests("题3 group_by_class", [
        (group_by_class(students),
         {"A": ["Bob", "Anna"], "B": ["Amy", "Cara"]},
         "按班分组、组内保序"),
    ])

    all_pass &= run_tests("题4 all_pairs", [
        (all_pairs(["A", "B", "C"]),
         [("A", "B"), ("A", "C"), ("B", "C")],
         "两两组合"),
        (all_pairs(["x"]), [], "不足两个为空"),
    ])

    all_pass &= run_tests("题5 prefix_sums", [
        (prefix_sums([1, 2, 3, 4]), [1, 3, 6, 10], "前缀和"),
        (prefix_sums([]), [], "空列表"),
    ])

    all_pass &= run_tests("题6 meal_combos", [
        (meal_combos(["饭", "面"], ["茶", "奶"]),
         [("饭", "茶"), ("饭", "奶"), ("面", "茶"), ("面", "奶")],
         "笛卡尔积套餐"),
        (meal_combos([], ["茶"]), [], "主菜为空"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！itertools 八个工具可以上手用了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")
