# ============================================================
# 第 28 课（练习）：collections 复习强化 —— 全部是新场景
# 运行方式：python 28_collections_review/28_collections_review_exercise.py
# ============================================================
from collections import defaultdict, Counter, namedtuple, deque

# 先读 28_collections_review.py，把四个工具再跑一遍。
# 下面 6 题只考 collections，场景都是新的。写完自检 ✅/❌。
# 卡住时：回知识文件看「小抄」和易错点，不要抄第 25 课 exercise 答案。

# ---------- 题 1：defaultdict(int) 统计字母 ----------
# 写 letter_counts(text: str) -> dict[str, int]
#   统计 text 里每个字符出现次数（含空格、标点，原样计）。
#   提示：defaultdict(int)，循环 ch in text: d[ch] += 1，最后 dict(d)。
def letter_counts(text: str) -> dict:
    pass


# ---------- 题 2：Counter 找 Top N 词频 ----------
# 写 top_words(words: list[str], n: int) -> list[tuple[str, int]]
#   words 是已分好的单词列表；返回出现次数最多的前 n 个 (词, 次数)。
#   次数相同时的顺序不要求与测试一致（most_common 按出现先后 tie-break）。
#   提示：Counter(words).most_common(n)
def top_words(words: list[str], n: int) -> list:
    pass


# ---------- 题 3：defaultdict(list) 按首字母分组 ----------
# 写 group_by_initial(names: list[str]) -> dict[str, list[str]]
#   把名字按首字母（小写）分组，组内名字保持输入顺序。
#   例：["Bob", "Amy", "Anna"] → {"b":["Bob"], "a":["Amy","Anna"]}
#   提示：key = name[0].lower()；defaultdict(list)；append。
def group_by_initial(names: list[str]) -> dict:
    pass


# ---------- 题 4：namedtuple 解析与更新 ----------
# 定义 namedtuple：Book，字段 title(str)、pages(int)。
# 写 parse_book(line: str) -> Book：
#   line 形如 "Python入门|320"（标题|页数），拆成 Book。
# 写 add_pages(book: Book, extra: int) -> Book：
#   页数增加 extra，返回新 Book（不能改原对象 —— 用 _replace）。
Book = namedtuple("Book", ["title", "pages"])


def parse_book(line: str):
    pass


def add_pages(book, extra: int):
    pass


# ---------- 题 5：deque 滑动窗口求平均 ----------
# 写 rolling_avg(nums: list[int], window: int) -> list[float]
#   对每个长度为 window 的连续子段算平均值（左端对齐，窗口不足时不输出）。
#   例：nums=[1,2,3,4,5], window=3 → [2.0, 3.0, 4.0]
#   提示：deque(maxlen=window)，每加入一个数，若 len==window 则 sum(window)/window。
def rolling_avg(nums: list[int], window: int) -> list:
    pass


# ---------- 题 6：综合 —— 日志里统计 IP + 每个 IP 的访问路径（去重） ----------
# 写 analyze_logs(rows: list[tuple[str, str]]) -> tuple[Counter, dict[str, set[str]]]
#   rows 每项是 (ip, path)，如 ("1.1.1.1", "/home")。
#   返回 (ip_counter, ip_paths)：
#     ip_counter：每个 IP 出现几次（用 Counter）
#     ip_paths：每个 IP 访问过哪些 path（去重，用 defaultdict(set)）
#   提示：两个结构各扫一遍 rows 即可。
def analyze_logs(rows: list[tuple[str, str]]) -> tuple:
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

    all_pass &= run_tests("题1 letter_counts", [
        (letter_counts("aab"), {"a": 2, "b": 1}, "简单计数"),
        (letter_counts(""), {}, "空串"),
    ])

    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    top2 = top_words(words, 2)
    all_pass &= run_tests("题2 top_words", [
        (len(top2), 2, "返回 2 项"),
        (top2[0], ("apple", 3), "第一名 apple×3"),
        (dict(top2), {"apple": 3, "banana": 2}, "前两名频次对"),
    ])

    all_pass &= run_tests("题3 group_by_initial", [
        (group_by_initial(["Bob", "Amy", "Anna", "bob"]),
         {"b": ["Bob", "bob"], "a": ["Amy", "Anna"]},
         "按首字母、保序"),
    ])

    all_pass &= run_tests("题4 parse_book / add_pages", [
        (parse_book("Python入门|320"), Book("Python入门", 320), "解析"),
        (add_pages(Book("X", 100), 50), Book("X", 150), "_replace 不改原对象"),
    ])

    all_pass &= run_tests("题5 rolling_avg", [
        (rolling_avg([1, 2, 3, 4, 5], 3), [2.0, 3.0, 4.0], "窗口3"),
        (rolling_avg([10], 3), [], "长度不足无输出"),
    ])

    rows = [
        ("1.1.1.1", "/home"),
        ("1.1.1.1", "/about"),
        ("2.2.2.2", "/home"),
        ("1.1.1.1", "/home"),   # 重复 path 只算一条
    ]
    cnt, paths = analyze_logs(rows)
    all_pass &= run_tests("题6 analyze_logs", [
        (dict(cnt), {"1.1.1.1": 3, "2.2.2.2": 1}, "IP 计数"),
        ({k: sorted(v) for k, v in paths.items()},
         {"1.1.1.1": ["/about", "/home"], "2.2.2.2": ["/home"]},
         "每 IP 路径去重"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！collections 四个工具可以上手用了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")
