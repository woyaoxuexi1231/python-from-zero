# ============================================================
# 第 13 课：函数进阶 —— 默认参数、*args、多返回值
# 运行方式：python 13_functions.py
# ============================================================

# 第 1 课会写函数，第 10 课会 return a, b。
# 这一课让调用更省事：常不变的参数给默认值；个数不固定时用 *args。


# ---------- 1. 默认参数：调用时可以不传 ----------
# 等号写在 def 的括号里，表示「没给就用这个」。
# 有默认值的参数必须放在没有默认值的后面。

def greet(name: str, suffix: str = "同学") -> str:
    return f"{name}{suffix}"


print(greet("小明"))  # 小明同学   用了默认
print(greet("小明", "老师"))  # 小明老师   传了就覆盖
print("-----")


# ---------- 2. 关键字参数：按名字传，不用记顺序 ----------
# 位置参数（按顺序）要写在关键字参数前面。

def letter(score: int, excellent: int = 90, passed: int = 60) -> str:
    if score >= excellent:
        return "优秀"
    elif score >= passed:
        return "及格"
    else:
        return "不及格"


print(letter(85))
print(letter(85, passed=80))  # 及格线改成 80，85 就不及格了
print(letter(95, excellent=98, passed=60))
print("-----")


# ---------- 3. *args：个数不固定的位置参数 ----------
# 名字前面加 *，函数里收到的是一个元组。
# 你自己写的时候，args 可以改成任何名字，习惯叫 args。

def add_all(*nums: int) -> int:
    result = 0
    for n in nums:
        result = result + n
    return result


print(add_all(1, 2))
print(add_all(1, 2, 3, 4))
print("-----")

# 已经有一个列表时，调用处加 * 可以拆开传进去：
print(add_all(*[10, 20, 30]))
print("-----")


# ---------- 4. 多返回值：复习一下 ----------
# return a, b 就是回一个元组。拆包接住。

def divmod_demo(a: int, b: int) -> tuple[int, int]:
    return a // b, a % b  # 整商，余数


q, r = divmod_demo(17, 5)
print(q)  # 3
print(r)  # 2
print("-----")


# ---------- 5. 默认值不要用空列表 ----------
# 默认值只在定义函数时算一次，不是每次调用算一次。
# 如果默认值是 [] / {}，多次调用会共用同一个列表，数据会串。
# 正确做法：默认写成 None，函数里面再新建。

def add_note(text: str, box: list[str] | None = None) -> list[str]:
    if box is None:
        box = []
    box.append(text)
    return box


print(add_note("第一句"))
print(add_note("另一句"))  # 另一份新列表，不会把第一句带过来
print("-----")


# ---------- 练习 ----------
# 1. 写函数 pad(text: str, n: int = 3) -> str
#    在 text 后面补 n 个句号。
#    pad("好")        应得到 好...
#    pad("好", 1)     应得到 好.
#    提示：text + "." * n
#
# 2. 写函数 longest(*words: str) -> str
#    在传入的若干字符串里，返回最长的那一个。
#    假设至少会传入一个词，不必处理空调用。
#    longest("hi", "hello", "hey")  应得到 hello
#    提示：先用 words[0] 当冠军，再 for 剩下的，更长就换掉。
#
# 写在下面，保存后再运行。


def pad(text: str, n: int = 3) -> str:
    while n > 0:
        text = text + "."
        n = n - 1
    return text


def pad2(text: str, n: int = 3) -> str:
    for i in range(n):
        text = text + "."
    return text


def pad3(text: str, n: int = 3) -> str:
    return text + "." * n


def longest(*words: str) -> str:
    longestW = ""
    for word in words:
        if len(word) > len(longestW):
            longestW = word
    return longestW

