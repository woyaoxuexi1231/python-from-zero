# ============================================================
# 第 17 课（复习课）：从 1 到 16 的大通关
# 运行方式：python 17_review.py
# ============================================================

# 这一课不教新东西。把前面学过的全串起来做一遍。
# 场景：一个学生成绩管理系统。下面每个函数对应几课的知识点。
# 函数骨架已经写好，你把 pass 换成实现，保存后运行看输出。
# 所有预期输出都标在注释里，对得上就说明那块真懂了。

from collections import defaultdict


# ---------- 题 1：函数 + 默认参数 + 返回多值（第 1、13 课）----------
# 写函数分析一个分数列表，返回 (最高分, 最低分, 平均分)。
# 平均分保留 1 位小数。空列表返回 (0, 0, 0.0)。
# analyze([90, 75, 40])  →  (90, 40, 68.3)
def analyze(scores: list[int]) -> tuple[int, int, float]:
    if len(scores) == 0:
        return (0, 0, 0.0)

    max = scores[0]
    min = scores[0]
    avg = 0
    sum = 0
    for score in scores:
        if score > max:
            max = score
        if score < min:
            min = score
        sum += score
    avg = round(sum / len(scores), 1)
    return max, min, avg


# ---------- 题 2：字符串 + 类型转换 + try/except（第 2、8 课）----------
# 写函数 safe_int(text: str, default: int = 0) -> int
# 能转成整数就转，转不了（比如 "abc"）就返回 default。
# safe_int("42")  →  42
# safe_int("abc") →  0
def safe_int(text: str, default: int = 0) -> int:
    try:
        i = int(text)
        return i
    except ValueError:
        return default


# ---------- 题 3：列表推导式 + 过滤（第 14 课）----------
# 写函数 passed_names(book: dict[str, int]) -> list[str]
# 返回所有及格(>=60)学生的名字，按名字长度从短到长排。
# 提示：推导式 + sorted(key=lambda n: len(n))
# passed_names({"小明":90,"hulei":75,"小红":40})  →  ["小明", "hulei"]
def passed_names(book: dict[str, int]) -> list[str]:
    score_ = [name for name, score in book.items() if score >= 60]
    return sorted(score_, key=lambda x: len(x))


# ---------- 题 4：集合去重 + 交集（第 10 课）----------
# 写函数 common_first_letters(names: list[str]) -> set[str]
# 返回所有名字首字母(忽略大小写)的集合。
# common_first_letters(["Bob","alice","Ben"])  →  {"b", "a"}
def common_first_letters(names: list[str]) -> set[str]:
    # 拿到所有的首字母合集
    return set(map(lambda x: x[:1].lower(), names))


# ---------- 题 5：lambda + sorted 多条件（第 15 课）----------
# 写函数 rank(book: dict[str, int]) -> list[tuple[str, int]]
# 按分数从高到低；同分按名字字母升序。返回 (名字, 分数) 列表。
# rank({"B":80,"A":90,"C":90})  →  [("A",90), ("C",90), ("B",80)]
def rank(book: dict[str, int]) -> list[tuple[str, int]]:
    # 分数降序用 -x[1]，同分(分数相同)再按名字 x[0] 升序
    return sorted(book.items(), key=lambda x: (-x[1], x[0]))


# ---------- 题 6：类与对象（第 16 课）----------
# 写 Student 类：属性 name、score；方法 is_pass() -> bool（>=60 及格）。
# 再写 __repr__ 让打印对象显示成 "名字:分数"。
class Student:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}:{self.score}"

    def __repr__(self):
        return self.__str__()

    def is_pass(self) -> bool:
        return self.score >= 60

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.name == other.name and self.score == other.score


# ---------- 题 7：综合 —— 把上面全用上（第 9~16 课融合）----------
# 写函数 top_students(book: dict[str, int], n: int) -> list[Student]
# 用 Student 类包住数据，按分数排前 n 名（高分在前），返回 Student 对象列表。
# 用题 6 的 Student。返回空列表若 n<=0。
# top_students({"A":90,"B":60,"C":80}, 2)  →  两个 Student: A(90), C(80)
def top_students(book: dict[str, int], n: int) -> list[Student]:
    # 先排序对象，然后筛选数量
    book_ = sorted(book.items(), key=lambda x: (x[1]), reverse=True)
    students: list[Student] = []
    if n > len(book_):
        n = len(book_)
    for i in range(n):
        students.append(Student(book_[i][0], book_[i][1]))

    return students


# ---------- 题 8：文件持久化（第 9 课）----------
# 写函数 save_book(book: dict[str, int], path: str) -> None
# 用 json.dump 写入文件（ensure_ascii=False, indent=2）。
# 写函数 load_book(path: str) -> dict[str, int]
# 读不到文件时返回空字典 {}（用 try/except FileNotFoundError）。
import json


def save_book(book: dict[str, int], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)


def load_book(path: str) -> dict[str, int]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# ---------- 题 9：while 菜单 + break（第 7 课）----------
# 写函数 run_menu(book: dict[str, int]) -> None
# 用 while True 做一个循环菜单：
#   输入 "1" → 打印成绩单（for name, score in book.items() 配合 letter 分档）
#   输入 "0" → 打印"再见"并 break 退出
#   其他输入 → 打印"没有这个选项"
# 不需要真的接 input()（避免交互），直接写逻辑，用一个模拟的 choice 列表驱动：
#   写一个内部 helper，或者就写函数体，下面验证里用给定序列测。
# 简化：写函数 handle(choice: str, book: dict[str, int]) -> str | None
#   "1" 返回成绩单字符串（每个 "名字:分数 等级"，用换行或空格连起来）
#   "0" 返回 "bye"（代表要退出）
#   其他输入 返回 "unknown"
# 可以用上面这个 letter() helper 给分数分档。
def letter(score: int) -> str:
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def handle(choice: str, book: dict[str, int]) -> str | None:
    result: str = ""
    if choice == "1":
        # for item in book.items():
        #     result+= f"{item[0]}:{item[1]} {letter(item[1])}\n"
        for k,v in book.items():
            result+= f"{k}:{v} {letter(v)}\n"
        return result
    elif choice == "0":
        return "bye"
    else:
        return "unknown"


# ============ 测试框架（不用改，你只写上面的函数）============
import json
import os


def run_tests(title: str, cases: list[tuple]) -> bool:
    """cases: [(期望值, 实际值, 说明), ...]，自动比对并打印。"""
    print(f"\n===== {title} =====")
    ok = 0
    for i, (expected, actual, desc) in enumerate(cases, 1):
        # 集合/列表顺序无关时按排序后比对
        def norm(v):
            # Student 对象默认按内存地址比较，转成 (name, score) 按内容比
            if hasattr(v, "name") and hasattr(v, "score"):
                return (v.name, v.score)
            if isinstance(v, list) and v and hasattr(v[0], "name") and hasattr(v[0], "score"):
                return sorted((s.name, s.score) for s in v)
            if isinstance(v, set):
                return sorted(v)
            if isinstance(v, list) and v and isinstance(v[0], (tuple, list)):
                return sorted(v)
            return v

        passed = norm(expected) == norm(actual)
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
    tmp = "review_tmp.json"
    if os.path.exists(tmp):
        os.remove(tmp)

    all_pass = True

    # 题1：analyze
    all_pass &= run_tests("题1 analyze（函数/返回多值/小数）", [
        (analyze([90, 75, 40]), (90, 40, 68.3), "常规[90,75,40]"),
        (analyze([60, 60, 60]), (60, 60, 60.0), "全相同"),
        (analyze([100]), (100, 100, 100.0), "单元素"),
        (analyze([0, 0, 0, 0]), (0, 0, 0.0), "全0"),
        (analyze([59, 61]), (61, 59, 60.0), "跨及格线"),
        (analyze([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), (10, 1, 5.5), "连续10个"),
        (analyze([-10, 10]), (10, -10, 0.0), "含负数"),
        (analyze([99, 100, 98]), (100, 98, 99.0), "高分段"),
        (analyze([42]), (42, 42, 42.0), "再来单元素"),
        (analyze([]), (0, 0, 0.0), "空列表返回(0,0,0.0)"),
    ])

    # 题2：safe_int
    all_pass &= run_tests("题2 safe_int（类型转换/try-except）", [
        (safe_int("42"), 42, '"42"'),
        (safe_int("abc"), 0, '"abc"用默认0'),
        (safe_int("0"), 0, '"0"'),
        (safe_int("-7"), -7, '"-7"负数'),
        (safe_int("3.14"), 0, '"3.14"非整数→默认'),
        (safe_int("10", 99), 10, '能转时忽略default'),
        (safe_int("xx", 5), 5, '转不了用default=5'),
        (safe_int("  88  "), 88, '首尾空格可转'),
        (safe_int(""), 0, '空串→默认'),
        (safe_int("1000000000000"), 1000000000000, '超大整数'),
    ])

    # 题3：passed_names
    all_pass &= run_tests("题3 passed_names（推导式+过滤+排序）", [
        (passed_names({"小明": 90, "hulei": 75, "小红": 40}), ["小明", "hulei"], "及格两人按长度"),
        (passed_names({"a": 59}), [], "全不及格→空"),
        (passed_names({"长名字": 60, "短": 90}), ["短", "长名字"], "长度升序"),
        (passed_names({}), [], "空字典"),
        (passed_names({"x": 60, "y": 60}), ["x", "y"], "同分按原序"),
        (passed_names({"张三": 100, "李": 80, "王": 30}), ["李", "张三"], "三字两字"),
        (passed_names({"A": 60, "B": 61, "C": 59}), ["A", "B"], "边界59/60/61"),
        (passed_names({"same": 70, "same2": 70}), ["same", "same2"], "同分稳序"),
        (passed_names({"一个": 90, "二": 90}), ["二", "一个"], "长度优先于分"),
        (passed_names({"zz": 100}), ["zz"], "单及格"),
    ])

    # 题4：common_first_letters
    all_pass &= run_tests("题4 common_first_letters（集合/首字母）", [
        (common_first_letters(["Bob", "alice", "Ben"]), {"a", "b"}, '忽略大小写'),
        (common_first_letters(["Amy", "Anna"]), {"a"}, "同首字母去重"),
        (common_first_letters([]), set(), "空列表→空集合"),
        (common_first_letters(["x", "X", "x"]), {"x"}, "全同字母"),
        (common_first_letters(["小明", "小红"]), {"小"}, "中文首字"),
        (common_first_letters(["Zoe", "zac", "yan"]), {"z", "y"}, "两字母"),
        (common_first_letters(["1a", "1b"]), {"1"}, "数字开头"),
        (common_first_letters(["A", "B", "C", "D"]), {"a", "b", "c", "d"}, "四个不同"),
        (common_first_letters(["Mike", "mike", "MIKE"]), {"m"}, "大小写混合"),
        (common_first_letters(["q", "w", "e", "r", "t", "y"]), {"q", "w", "e", "r", "t", "y"}, "六个不同"),
    ])

    # 题5：rank
    all_pass &= run_tests("题5 rank（lambda/多条件排序）", [
        (rank({"B": 80, "A": 90, "C": 90}), [("A", 90), ("C", 90), ("B", 80)], "同分按名字"),
        (rank({"x": 50}), [("x", 50)], "单元素"),
        (rank({}), [], "空字典"),
        (rank({"a": 60, "b": 60, "c": 60}), [("a", 60), ("b", 60), ("c", 60)], "全同分"),
        (rank({"z": 10, "y": 20, "x": 30}), [("x", 30), ("y", 20), ("z", 10)], "倒序名"),
        (rank({"m": 100, "n": 99, "o": 98}), [("m", 100), ("n", 99), ("o", 98)], "降序"),
        (rank({"aa": 70, "ab": 70, "ac": 70}), [("aa", 70), ("ab", 70), ("ac", 70)], "同分三字"),
        (rank({"A": 1, "B": 2}), [("B", 2), ("A", 1)], "最小分"),
        (rank({"p": 88, "q": 88, "r": 87}), [("p", 88), ("q", 88), ("r", 87)], "两同分一低"),
        (rank({"k": 60, "j": 90, "i": 75}), [("j", 90), ("i", 75), ("k", 60)], "乱序输入"),
    ])

    # 题6：Student 类
    s_ok = True
    s_cases = []
    try:
        a = Student("小明", 90)
        b = Student("小红", 40)
        s_cases.append((("小明", 90), (a.name, a.score), "属性存取"))
        s_cases.append((True, a.is_pass(), "90及格"))
        s_cases.append((False, b.is_pass(), "40不及格"))
        s_cases.append((True, Student("边界", 60).is_pass(), "60及格边界"))
        s_cases.append((False, Student("边界", 59).is_pass(), "59不及格边界"))
        s_cases.append(("小明:90", repr(a), "__repr__格式"))
        s_cases.append(("小红:40", repr(b), "__repr__另一个"))
        s_cases.append((True, Student("x", 100).is_pass(), "满分及格"))
        s_cases.append((False, Student("y", 0).is_pass(), "0分"))
        s_cases.append(("小明:90", str(a), "str与repr一致"))
    except Exception as e:
        s_ok = False
        print(f"\n===== 题6 Student 类 =====\n  ❌ 构造/调用抛异常: {e!r}")
    if s_cases:
        all_pass &= run_tests("题6 Student 类（__init__/self/__repr__）", s_cases)
    else:
        all_pass &= s_ok

    # 题7：top_students
    all_pass &= run_tests("题7 top_students（综合：类+排序+切片）", [
        (top_students({"A": 90, "B": 60, "C": 80}, 2), [Student("A", 90), Student("C", 80)], "取前2"),
        (top_students({"A": 90}, 5), [Student("A", 90)], "n超出人数"),
        (top_students({"A": 90, "B": 60}, 0), [], "n=0→空"),
        (top_students({"A": 90, "B": 60}, -1), [], "n<0→空"),
        (top_students({}, 3), [], "空字典"),
        (top_students({"x": 70, "y": 70}, 1), [Student("x", 70)], "同分取其一(稳序)"),
        (top_students({"low": 10, "high": 99}, 2), [Student("high", 99), Student("low", 10)], "高低排序"),
        (top_students({"m": 50, "n": 100, "o": 75}, 3), [Student("n", 100), Student("o", 75), Student("m", 50)],
         "三段"),
        (top_students({"a": 60}, 1), [Student("a", 60)], "边界及格"),
        (top_students({"p": 80, "q": 80, "r": 80}, 2), [Student("p", 80), Student("q", 80)], "全同分取前2"),
    ])

    # 题8：save/load_book
    t8 = []
    try:
        save_book({"测试": 88, "小明": 90}, tmp)
        t8.append(({"测试": 88, "小明": 90}, load_book(tmp), "写入后能读回"))
        save_book({}, tmp)
        t8.append(({}, load_book(tmp), "空字典读写"))
        t8.append(({}, load_book("不存在的文件.json"), "读不到→空字典"))
        save_book({"a": 1}, tmp)
        t8.append(({"a": 1}, load_book(tmp), "单键值"))
        save_book({"中文名": 100}, tmp)
        t8.append(({"中文名": 100}, load_book(tmp), "中文key(ensure_ascii)"))
        save_book({"x": 0, "y": -5}, tmp)
        t8.append(({"x": 0, "y": -5}, load_book(tmp), "含0和负"))
        save_book({"big": 999999}, tmp)
        t8.append(({"big": 999999}, load_book(tmp), "大数"))
        save_book({"same": 60, "same2": 60}, tmp)
        t8.append(({"same": 60, "same2": 60}, load_book(tmp), "同分两键"))
        save_book({"z": 1, "a": 2}, tmp)
        t8.append(({"z": 1, "a": 2}, load_book(tmp), "乱序key保持"))
        save_book({"only": 42}, tmp)
        t8.append(({"only": 42}, load_book(tmp), "最后一例"))
    except Exception as e:
        print(f"\n===== 题8 文件持久化 =====\n  ❌ 抛异常: {e!r}")
        t8 = []
    all_pass &= run_tests("题8 save/load_book（JSON读写/异常）", t8)

    # 题9：handle（菜单逻辑）
    all_pass &= run_tests("题9 handle（while菜单逻辑/分档）", [
        ("优秀" in handle("1", {"小明": 90}) and "90" in handle("1", {"小明": 90}), True, '"1"含名字分数等级'),
        (handle("0", {}), "bye", '"0"返回bye'),
        (handle("x", {"小明": 90}), "unknown", "其他→unknown"),
        (handle("2", {"a": 60}), "unknown", '"2"也是unknown'),
        ("及格" in handle("1", {"生": 60}), True, '"1"边界60→及格'),
        ("不及格" in handle("1", {"生": 59}), True, '"1"边界59→不及格'),
        (handle("", {}), "unknown", '空串→unknown'),
        ("优秀" in handle("1", {"满": 100}), True, '"1"满分→优秀'),
        (handle("0", {"很多": 1, "数据": 2}), "bye", '"0"忽略book'),
        (handle("1", {}) == "" or handle("1", {}) is not None and "优秀" not in handle("1", {}), True, "空book不崩"),
    ])

    if os.path.exists(tmp):
        os.remove(tmp)

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部 9 题、90 个用例通过！1~16 课复习通关！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应函数，再跑一次。")
