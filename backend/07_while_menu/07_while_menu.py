# ============================================================
# 第 7 课：while 循环和菜单
# 运行方式：python 07_while_menu.py
# ============================================================

# 第 6 课的成绩本是一条直线：打印 → 查一次 → 加一次 → 结束。
# 真正的小程序会转圈：做完一件事回到菜单，直到你选退出。
#
# for：事先知道要走几遍（列表有几项，就转几圈）。
# while：事先不知道转几圈，条件还成立就继续。


# ---------- 1. while：条件成立就再来一遍 ----------
# 和 if 很像：后面跟一个条件，缩进的那几行属于这个循环。
# 不同的是：跑完会回到 while 再问一次条件。

count = 3
while count > 0:
    print(count)
    count = count - 1
print("到 0 了，循环结束")
print("-----")


# ---------- 2. while True + break ----------
# True 永远成立，这个循环会一直转。
# break 的意思是：立刻跳出当前循环，不管条件还成不成立。
#
# 这是做菜单最常用的写法：
#   永远等用户选；选了退出，就 break。

n = 1
while True:
    print(n)
    if n == 3:
        break
    n = n + 1
print("碰到 3 就停了")
print("-----")


# ---------- 3. continue：跳过这一圈剩下的部分 ----------
# break 是离开整个循环。
# continue 是结束这一圈，马上开始下一圈。
# 下面会打印 1 2 4 5，3 被跳过。

n = 0
while n < 5:
    n = n + 1
    if n == 3:
        continue
    print(n)
print("-----")


# ---------- 4. 菜单：把 while 和 if 拼起来 ----------
# input() 拿到的永远是字符串，所以和 "1" 比，不要和 1 比。
# 选错了走 else，提示一下，循环会自动再打印菜单。
#
# 成绩本的函数和第 6 课一样，这一课只改「主流程」。

scores: dict[str, int] = {
    "小明": 90,
    "hulei": 75,
    "小红": 40,
}


def add_score(book: dict[str, int], name: str, score: int) -> None:
    book[name] = score


def get_score(book: dict[str, int], name: str) -> int | None:
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


def average_score(book: dict[str, int]) -> float:
    result = 0
    for name, score in book.items():
        result = result + score
    return result / len(book)


def passed_names(book: dict[str, int]) -> list[str]:
    names: list[str] = []
    for name, score in book.items():
        if score >= 60:
            names.append(name)
    return names


def print_menu() -> None:
    print()
    print("1. 查看成绩单")
    print("2. 查询一个人")
    print("3. 新增/修改")
    print("4. 平均分和及格名单")
    print("0. 退出")


# ---------- 程序从这里开始跑 ----------
# 现在只接好了 1 和 0。跑起来先玩这两项，确认能反复进菜单、能退出。
# 2、3、4 是练习，自己接到 elif 上。

while True:
    print_menu()
    choice = input("请选择：")

    if choice == "1":
        print_report(scores)
    elif choice == "2":
        lookup()
    elif choice == "3":
        add_one()
    elif choice == "4":
        print(f"平均分: {average_score(scores)}")
        print(f"及格的人有: {passed_names(scores)}")
    elif choice == "0":
        print("再见")
        break
    else:
        print("没有这个选项")


# ---------- 练习 ----------
# 1. 在 if choice == "1" 后面加：
#        elif choice == "2":
#            lookup()
#        elif choice == "3":
#            add_one()
#    保存后再运行。选 2 能查人，选 3 能改分数，改完再选 1 能看见变化。
#
# 2. 再加选项 4：打印平均分，再打印及格的人。
#        elif choice == "4":
#            ...
#    提示：average_score(scores) 和 passed_names(scores) 已经写好了，
#    用 f-string print 出来即可。
#
# 输入不是数字时程序还会崩，下一课再处理。先把菜单转圈跑顺。
