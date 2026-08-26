# ============================================================
# 第 9 课：文件和 JSON —— 关掉程序，数据还在
# 运行方式：python 09_files_json.py
# 请在 from-zero 目录下运行，生成的文件会出现在同一目录。
# ============================================================

# 到目前为止，成绩只活在内存里。程序一结束，改过的分数就没了。
# 这一课把字典写进文件，下次启动再读回来。
#
# 新东西只有三件：
#   1. import        借用 Python 自带的工具
#   2. with open(...) 打开文件，用完自动关
#   3. json.dump / json.load   字典 ⇄ 文本文件


# ---------- 1. import ----------
# json 是 Python 自带的，不用 pip 安装。
# 文件开头写一次，后面都能用。

import json


# ---------- 2. 先写一个普通文本文件，再读出来 ----------
# "w" 表示写入（文件已有内容会被整份覆盖）。
# encoding="utf-8" 必须写。Windows 上不写，中文常常是乱码。
# with 的意思：这个块结束时，文件自动关掉。不要自己记着 close。

with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("你好，文件")

with open("demo.txt", encoding="utf-8") as f:
    text = f.read()
print(text)
print("-----")

# ---------- 3. JSON：专门用来保存 dict / list ----------
# JSON 是一种文本格式。长得像 Python 字典，但能放进文件、给别的语言读。
# json.dump(数据, 文件)  写入
# json.load(文件)        读出，得到字典
#
# ensure_ascii=False  让中文原样写入。不写的话文件里会变成 \u5c0f\u660e。
# indent=2            换行缩进，方便你打开文件看。

demo = {"hulei": 75, "小明": 90}
with open("demo.json", "w", encoding="utf-8") as f:
    json.dump(demo, f, ensure_ascii=False, indent=2)

with open("demo.json", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)
print(loaded["hulei"])
print("-----")
print("现在去文件夹里打开 demo.json 看一眼，再回来。")
print("-----")


# ---------- 4. 文件不存在怎么办 ----------
# 第一次跑还没有 scores.json，直接读会 FileNotFoundError。
# 第 8 课的 try / except 在这里正好用上：没有文件就用默认成绩。


def load_scores() -> dict[str, int]:
    try:
        with open("scores.json", encoding="utf-8") as f:
            data = json.load(f)
        print("已从 scores.json 读入成绩")
        return data
    except FileNotFoundError:
        print("还没有 scores.json，使用默认成绩")
        return {
            "小明": 90,
            "hulei": 75,
            "小红": 40,
        }


def save_scores(book: dict[str, int]) -> None:
    with open("scores.json", "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)
    print("已写入 scores.json")


# ---------- 5. 成绩本（第 8 课的菜单 + 读文件）----------
# 启动时读一次。保存还没接上，这是练习。

scores = load_scores()


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
    while True:
        score_text = input("分数是多少？")
        try:
            score = int(score_text)
            break
        except ValueError:
            print("请输入整数")
    add_score(scores, name, score)
    # # 把数据持久化，① 打开文件
    # with open("scores.json", "w", encoding="utf-8") as f:
    #     # ② 使用json格式存储
    #     json.dump(scores, f, ensure_ascii=False, indent=2)
    save_scores(scores)

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
        # 退出前也保存一次文件信息
        # with open("scores.json", "w", encoding="utf-8") as f:
        #     json.dump(scores, f, ensure_ascii=False, indent=2)
        save_scores(scores)
        print("再见")
        break
    else:
        print("没有这个选项")

# ---------- 练习 ----------
# 1. 在 add_one 里，打印「已保存」之后调用：
#        save_scores(scores)
#    函数已经写好了，接上即可。
#
#    验证：选 3 加一个新人（比如 小刚 60），选 0 退出。
#    再运行一次 python 09_files_json.py，选 1，应能看见小刚。
#    也可以直接打开 scores.json 看内容。
#
# 2. 选 0 退出之前也调用一次 save_scores(scores)。
#    现在改完立刻写盘；退出时再写一次，两种习惯都认识一下。
#    第一次跑没有 scores.json 是正常的，except FileNotFoundError 会走默认成绩。
