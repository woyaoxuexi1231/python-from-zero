# ============================================================
# 第 25 课（练习）：常用数据结构 + itertools —— 全部是新场景
# 运行方式：python 25_collections_itertools/25_collections_itertools_exercise.py
# ============================================================
from collections import defaultdict, namedtuple
import itertools

# 先读 25_collections_itertools.py 学工具用法。
# 下面 5 个是新场景：不让你抄示例，而是把 defaultdict/计数器/namedtuple/
# itertools 用到别的地方去。写完自检 ✅/❌。

# ---------- 题 1：倒排索引（defaultdict 建"单词→行号列表"） ----------
# 场景：搜索引擎要给每行文本建立"单词出现在哪些行"的索引。
# 写 build_index(lines)：lines 是若干行文本(list[str])。
#   对每一行，按空格拆成单词，把"当前行号"记到该单词名下。
#   返回 dict：{ 单词: 出现过的行号列表(升序、去重) }。
#   提示：用 defaultdict(set) 收集行号（集合天然去重），最后把每个单词的
#        集合转成已排序的 list。
def build_index(lines: list[str]) -> dict:
    pass   # 填


# ---------- 题 2：按班取最高分（defaultdict 分组 + max） ----------
# 场景：一堆学生记录 (班级, 分数)，要算每个班的最高分。
# 写 top_by_class(records)：records 是 list[tuple[str,int]]，形如 [("A",80),...]。
#   返回 dict：{ 班级: 该班最高分 }。
#   提示：先按班分组(把分数收进 list 或直接活的 max)，再求每组最大值。
def top_by_class(records: list[tuple[str, int]]) -> dict:
    pass   # 填


# ---------- 题 3：namedtuple 找最强的回购（读写字段） ----------
# 场景：用轻量元组存"开源项目"数据，选出 stars 最高的那个。
# 写一个 namedtuple 类型 Repo，字段为 name 和 stars。
# 再写 max_stars(repos)：给定一批 Repo，返回 stars 最高者的 name。
#   提示：name = namedtuple("Repo", ...)；遍历时用 r.stars 访问字段。
def max_stars(repos: list) -> str:
    pass   # 填


# ---------- 题 4：惰性取前 N 个（itertools.islice 截取） ----------
# 场景：有个无限或很大的生成器，只想拿前 N 个，不想全展开。
# 写 take_first(n, it)：用 itertools.islice 取可迭代对象 it 的前 n 个，返回 list。
#   提示：list(itertools.islice(it, n))。
def take_first(n: int, it) -> list:
    pass   # 填


# ---------- 题 5：笛卡尔排列（itertools.product） ----------
# 场景：用字符集生成长度为 k 的"所有"串 combos，且允许重复。
# 写 arrangements(alphabet, k)：返回所有长度为 k 的串的 list，
#   字符可重复、顺序区分（如 alphabet="AB"、k=2 → AA,AB,BA,BB）。
#   提示：for t in itertools.product(alphabet, repeat=k):  ，t 是字符元组，join 一下。
def arrangements(alphabet: str, k: int) -> list:
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


if __name__ == "__main__":
    all_pass = True

    # ---- 题1：倒排索引 ----
    lines = [
        "apple banana",                  # 行0
        "banana",                        # 行1
        "apple banana apple",            # 行2
    ]
    all_pass &= run_tests("题1 倒排索引 build_index", [
        (build_index(lines),
         {"apple": [0, 2], "banana": [0, 1, 2]},
         "按行号升序、去重"),
    ])

    # ---- 题2：按班取最高分 ----
    records = [("A", 80), ("B", 70), ("A", 95), ("C", 60), ("B", 88)]
    all_pass &= run_tests("题2 按班最高分 top_by_class", [
        (top_by_class(records),
         {"A": 95, "B": 88, "C": 60},
         "每班取最高分"),
    ])

    # ---- 题3：namedtuple 找最高 star ----
    Repo = namedtuple("Repo", ["name", "stars"])
    all_pass &= run_tests("题3 max_stars(namedtuple)", [
        (max_stars([
            Repo("torvalds/linux", 140_000),
            Repo("tensorflow/tensorflow", 170_000),
            Repo("vscxx/repo", 10),
        ]), "tensorflow/tensorflow", "挑 star 最多的"),
        (max_stars([Repo("a/b", 1)]), "a/b", "单元素也能跑"),
    ])

    # ---- 题4：惰性取前 N ----
    def naturals():
        i = 0
        while True:
            yield i
            i += 1
    all_pass &= run_tests("题4 take_first(islice)", [
        (take_first(5, naturals()), [0, 1, 2, 3, 4], "无限生成器只取前5"),
        (take_first(10, [1, 2]), [1, 2], "比 n 短时取完即止，不报错"),
    ])

    # ---- 题5：笛卡尔排列 ----
    all_pass &= run_tests("题5 arrangements(product)", [
        (arrangements("AB", 2), ["AA", "AB", "BA", "BB"], "字符集AB长度2的全部串"),
        (arrangements("xy", 1), ["x", "y"], "长度1"),
        (len(arrangements("abc", 3)), 27, "3字符×3长度 = 3^3=27 个"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！集合/计数/命名元组/迭代器工具都通用了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")