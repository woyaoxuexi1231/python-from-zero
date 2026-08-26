# ============================================================
# 第 6 课：成绩本 —— 把前五课拼起来
# 运行方式：python 06_gradebook.py
# ============================================================

# 一个小程序通常长这样：
#   1. 数据（这里是成绩字典）
#   2. 几个各干一件事的函数
#   3. 从输入到输出的主流程
#
# 你已经会的东西都会用到：
#   变量、类型、函数返回值、input、if、列表、字典、for

scores: dict[str, int] = {
    "小明": 90,
    "hulei": 75,
    "小红": 40,
}


def add_score(book: dict[str, int], name: str, score: int) -> None:
    """把一个人的分数写进成绩本。有则改，无则加。"""
    book[name] = score


def get_score(book: dict[str, int], name: str) -> int | None:
    """找到就返回分数；找不到返回 None（表示没有）。"""
    if name in book:
        return book[name]
    else:
        return None


def letter(score: int) -> str:
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def print_report(book: dict[str, int]) -> None:
    print("----- 成绩单 -----")
    for name, score in book.items():
        print(f"{name}: {score} 分，{letter(score)}")
    print("-----------------")


def lookup() -> None:
    name = input("要查询谁的分数？")
    score = get_score(scores, name)
    if score is None:
        print(f"没有 {name} 这个人")
    else:
        print(f"{name} 是 {score} 分，{letter(score)}")


def add_one() -> None:
    name = input("新增/修改谁？")
    score_text = input("分数是多少？")
    score = int(score_text)
    add_score(scores, name, score)
    print(f"已保存：{name} = {score}")


# 返回所有分数的平均分
def average_score(book: dict[str, int]) -> float | None:
    # 记录总分数
    result = 0
    for k, v in book.items():
        result += v
    return result / len(book)


# 返回所有及格的人
def passed_names(book: dict[str, int]) -> list[str]:
    names: list[str] = []
    for k, v in book.items():
        if v >= 60:
            names.append(k)
    return names


# ---------- 程序从这里开始跑 ----------
print_report(scores)
lookup()
add_one()
print_report(scores)
print(f"平均分: {average_score(scores)}")
print(f"及格的人有: {passed_names(scores)}")

# ---------- 练习 ----------
# 1. 写函数 average_score(book: dict[str, int]) -> float
#    返回平均分（总分除以人数）。
#    提示：total / len(book)  除法的结果是 float。
#
# 2. 写函数 passed_names(book: dict[str, int]) -> list[str]
#    返回所有分数 >= 60 的人的名字，做成一个列表。
#    提示：先准备空列表 names: list[str] = []，
#    循环里用 if 判断，合格就 names.append(name)。
#
# 两个函数都写好后：
#    print(average_score(scores))
#    print(passed_names(scores))
# 写在下面，保存后再运行。
