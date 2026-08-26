# ============================================================
# 第 3 课：if / else 判断
# 运行方式：python 03_if_else.py
# ============================================================

# ---------- 1. 比较的结果是 True 或 False ----------
# 一个等号 =  是赋值（把右边放进左边）
# 两个等号 == 是比较（问：两边相不相等？）

print(3 > 1)  # True
print(18 >= 18)  # True
print(3 == 5)  # False
print(3 != 5)  # True   != 表示「不等于」
print("-----")

# ---------- 2. if / else ----------
# if 后面跟一个条件。条件为 True 时，执行缩进的那几行。
# 否则走 else。
# Python 用缩进（前面空 4 格）表示「属于这个 if」。少空、多空都会报错。

age = 20
if age >= 18:
    print("成年")
else:
    print("未成年")
print("-----")

# ---------- 3. elif：多个分支 ----------
# elif 是 else if 的缩写，意思是「上面都不对，再试这个」。
# 从上往下看，命中第一个 True 就停，后面不再跑。

score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
print("-----")


# ---------- 4. 在函数里判断，并返回结果 ----------

def is_adult(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False


print(is_adult(20))  # True
print(is_adult(15))  # False
print("-----")


def grade(score: int) -> str:
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


print(grade(95))
print(grade(70))
print(grade(40))
print("-----")

# ---------- 5. 和 input 拼起来 ----------

user_age_text = input("请输入年龄：")
user_age = int(user_age_text)

if is_adult(user_age):
    print(f"{user_age} 岁，已经成年")
else:
    print(f"{user_age} 岁，还未成年")


# ---------- 练习 ----------
# 1. 写一个函数 abs_value(n: int) -> int
#    如果 n >= 0，返回 n；否则返回 -n。
#    例如 abs_value(-5) 应该得到 5。
#
# 2. 用 input 问用户一个整数，调用 abs_value，用 f-string 打印结果。
#
# 写在下面，保存后再运行。


def abs_value(n: int) -> int:
    if n >= 0:
        return n
    else:
        return 0 - n


abs_value(4)
abs_value(-3)

myNum = input("请输入一个整数: ")
# 转换成数字先
myNumint = int(myNum)
myNumAbs = abs_value(myNumint)
print(f"绝对值是: {myNumAbs}")
