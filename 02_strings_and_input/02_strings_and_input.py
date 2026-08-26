# ============================================================
# 第 2 课：字符串、输入、类型转换
# 运行方式：python 02_strings_and_input.py
# 这一课会问你问题，在终端里输入后按回车。
# ============================================================

# ---------- 1. 字符串可以拼起来 ----------
# + 用在数字上是加法：3 + 5 -> 8
# + 用在字符串上是拼接："你" + "好" -> "你好"

first = "hu"
last = "lei"
full = first + last
print(full)          # hulei
print("-----")


# ---------- 2. 数字和文字不能直接用 + 拼 ----------
# 下面这行如果取消注释会报错：
# print("年龄是" + 18)
# 因为左边是 str，右边是 int，类型不一样。
# 解决办法：先把数字变成字符串。

age = 18
print("年龄是" + str(age))
print("-----")


# ---------- 3. f-string：更常用的写法 ----------
# 在字符串前面加 f，用 {变量} 把值嵌进去。
# 这是现在写 Python 最常见的方式，记住它。

name = "hulei"
print(f"我叫{name}，今年{age}岁")
print("-----")


# ---------- 4. input()：从终端读入文字 ----------
# input("提示语") 会停下来等你打字，按回车后，
# 你打的内容会作为字符串返回。
#
# 注意：无论你输入 18 还是 hello，得到的永远是 str。

user_name = input("请输入你的名字：")
print(f"你好，{user_name}")
print(type(user_name))
print("-----")


# ---------- 5. 想拿数字，必须自己转类型 ----------
# int("18")   把字符串变成整数
# float("1.75") 把字符串变成小数
# str(18)     把数字变成字符串

age_text = input("请输入你的年龄：")
age_number = int(age_text)
print(type(age_text))      # <class 'str'>   还没转之前
print(type(age_number))    # <class 'int'>   转完之后
print(f"明年你 {age_number + 1} 岁")
print("-----")


# ---------- 6. 把输入和函数拼起来 ----------

def next_year(current_age: int) -> int:
    return current_age + 1


print(f"再用函数算一次：明年 {next_year(age_number)} 岁")


# ---------- 练习 ----------
# 1. 再问一次用户：请输入一个数字。
# 2. 写一个函数 double(n: int) -> int，返回 n 的两倍。
# 3. 用 f-string 打印：你输入的是 X，两倍是 Y
#
# 写在下面，保存后再运行。

myNum = input("请输入一个数字：")

def double(n: int) -> int:
    return n * 2

# 把字符串转成数字
myNum2 = int(myNum)
print(f"你输入的数字是: {myNum}, 这个数字的两倍是 {double(myNum2)}")