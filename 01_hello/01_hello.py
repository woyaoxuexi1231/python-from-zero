# ============================================================
# 第 1 课：你好，Python
# 运行方式：python 01_hello.py
# ============================================================

# ---------- 1. 打印 ----------
# print() 会把括号里的内容显示到终端。
# 字符串要用引号包起来：'单引号' 或 "双引号" 都可以。

print("你好，Python")
print("-----")


# ---------- 2. 变量 ----------
# 变量 = 给一个值起名字，方便后面反复使用。
# Python 不需要先声明类型，写名字、写等号、写值即可。

name = "小明"
age = 18
height = 1.75
is_student = True

print(name)
print(age)
print(height)
print(is_student)
print("-----")


# ---------- 3. 基本类型 ----------
# 每个值都有类型。常用的有 4 种：
#   str   字符串   "hello"
#   int   整数     18
#   float 小数     1.75
#   bool  布尔     True / False   （注意首字母大写）
#
# type() 可以查看一个值的类型。

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>
print("-----")


# ---------- 4. 函数：做什么、返回什么 ----------
# def 用来定义函数。
# 函数可以接收参数（括号里的东西），也可以返回结果（return）。
#
# 下面这个函数：
#   名字：add
#   参数：a 和 b，都是整数
#   返回：它们的和，也是整数
#
# a: int     表示「我希望 a 是整数」——这叫类型标注，给人和工具看的
# -> int     表示「这个函数返回整数」
# 类型标注不是必须的。Python 不写也能跑。写上是为了让代码更清楚。

def add(a: int, b: int) -> int:
    result = a + b
    return result


# 调用函数：写函数名，把真正的数字传进去。
# 返回值可以存进变量，也可以直接 print。

total = add(3, 5)
print(total)          # 8
print(add(10, 20))    # 30
print("-----")


# 不写类型标注，效果完全一样：
def add_without_types(a, b):
    return a + b


print(add_without_types(1, 2))
print("-----")


# ---------- 5. 没有返回值的函数 ----------
# 有的函数只是做事（比如打印），不需要 return。
# 这时返回值类型可以写成 None。

def greet(person: str) -> None:
    print("你好，" + person)


greet(name)


# ---------- 练习（自己改，再运行）----------
# 1. 把 name 改成你自己的名字，再运行，看输出变了没有。
# 2. 自己写一个函数 multiply，接收两个整数，返回它们的乘积。
# 3. 调用 multiply(6, 7)，把结果 print 出来，应该是 42。


myname = "hulei"
print(myname)

def multiply(num1: int, num2: int) -> int:
    return num1 * num2

print(multiply(6, 7))