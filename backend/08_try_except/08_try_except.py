# ============================================================
# 第 8 课：try / except —— 出错时别让程序崩掉
# 运行方式：python 08_try_except.py
# ============================================================

# 第 7 课的菜单已经能转圈了。
# 但选 3 新增分数时，如果你输入 abc，int("abc") 会直接崩溃，菜单也没了。
#
# 这一课只干一件事：把「会崩的那一行」包起来，失败就提示，然后继续跑。


# ---------- 1. 哪些操作会崩 ----------
# int() 只吃「看起来像整数」的字符串。

print(int("18"))  # 18，正常
print("-----")

# 下面这行如果取消注释，程序会在这里停死，后面的代码都不会跑：
# print(int("abc"))
# 报错名字叫 ValueError（值不对）


# ---------- 2. try / except ----------
# try 下面放可能出错的代码。
# 出错了就跳到 except，不会崩。
# except 后面要写错误的类型，这里是 ValueError。
#
# Java 里类似：try { } catch (NumberFormatException e) { }

try:
    print(int("abc"))
except ValueError:
    print("这不是整数")

print("程序还在跑")  # 这句话会打印，说明没有崩
print("-----")

# ---------- 3. 成功走 try，失败走 except ----------
# 同一个结构，换一个合法的字符串，就不会进 except。

try:
    print(int("20"))
except ValueError:
    print("这不是整数")
print("-----")

# ---------- 4. except 要写具体类型 ----------
# 不要写成 except:  那种会把所有错误都吃掉，包括你自己写错的 bug。
# 现在只要记住：int() 转失败 → ValueError。


# ---------- 5. 成绩本：第 7 课的菜单原样留下 ----------
# add_one 里的 int(score_text) 还是会崩。这是练习要改的地方。
# 改完之后：输入 abc，应该看到提示，然后回到菜单，而不是程序消失。

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
    score = 0
    end = False
    while not end:
        try:
            score_text = input("分数是多少？")
            score = int(score_text)
            end = True
        except ValueError:
            print("请输入正确的成绩")
            end = False

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
# 1. 改 add_one：把 int(score_text) 包进 try / except ValueError。
#    失败时 print("请输入整数")，然后 return（函数结束，回到菜单）。
#    成功时保持原来的：写入成绩本并打印「已保存」。
#
#    跑起来验证：选 3，分数输入 abc，应提示后回到菜单；
#    再选 3，分数输入 88，应保存成功。
#
# 2. 不要失败就放弃。分数不合法时继续问，直到输入的是整数。
#    提示：在 add_one 里用 while True，try 成功就 break，失败就 print 然后继续循环。
#    这是第 7 课 while + 第 8 课 try 的组合，菜单本身就是这个套路。
