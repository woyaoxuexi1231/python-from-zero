# ============================================================
# 第 19 课：迭代器与生成器（iter / next / yield）
# 运行方式：python 19_iterators_generators/19_iterators_generators.py
# ============================================================


# 前面你一直在写 `for x in ...`。有没有想过 for 到底是怎么「一个一个取」的？
# 这一课扒开 for 的皮，看看它背后的机制：
#   - 迭代器(iterator)：每次只吐一个，取完就没了
#   - 生成器(generator)：用 yield 写的「惰性」迭代器，按需现算
#   你写 Java：Java 有 Iterator<T>，接口是 hasNext() + next()；
#   Python 简化成一个 next()，取到头抛 StopIteration；再配合 yield 还能写成
#   生成器函数（Java 到 Java 19 才有的概念，Python 一直都有）。
#
# 核心收获：不是把所有结果一次算好装进内存，而是一个一个地算。
# 数据大、或者无限循环时，这是救命的关键。

# ---------- 0. 先回顾：什么样的东西能被 for 循环 ----------
# 列表、字符串、字典、range……只要「能一个一个取出来」就可以。
# 这种"能一个一个取"的对象，叫可迭代对象(iterable)。
for x in [1, 2, 3]:
    print(x)  # 1 2 3
for ch in "abc":
    print(ch)  # a b c
print("-----")

# ---------- 1. for 循环背后的真相：iter() + next() ----------
# 你以为 for 是魔法？其实它分两步：
#   1) iter(对象)  拿到一个"迭代器"
#   2) 不断 next(迭代器) 取下一个值，取完抛出 StopIteration，for 就收工
# 下面手动用一句句 next 复刻 for 的行为：

nums = [10, 20, 30]
it = iter(nums)  # 拿到迭代器
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it))        # 到这里再取就会抛 StopIteration（注释掉，避免崩）

# 用 try/except 接住结束信号，就完全等价于 for 循环了：
it2 = iter(nums)
while True:
    try:
        print(next(it2))
    except StopIteration:
        print("取完了")
        break
# 10 / 20 / 30 / 取完了
print("-----")

# ---------- 2. 迭代器是一次性的 ----------
# 迭代器记住自己的位置，取一个就往前走一步，不能回头。
# 注意：range / 列表本身不是迭代器，iter() 出来的才算。列表能重来，迭代器不行。
lst = [1, 2, 3]
it = iter(lst)
print(list(it))  # [1, 2, 3]  第一次，能取到
print(list(it))  # []         第二次，已经空啦（迭代器用完了）
# 而列表本身可以反复 for：
print("列表可以反复用：")
for x in lst:
    pass  # 只是演示，不打印
for x in lst:
    pass
print("-----")


# ---------- 3. 自己写一个迭代器类 ----------
# 想让一个类能被 for 循环，只需实现两个方法：
#   __iter__(self) -> 返回迭代器（通常就是 self）
#   __next__(self) -> 返回下一个值；没得取时抛 StopIteration

class Countdown:
    """从 n 数到 1 的倒计时迭代器。"""

    def __init__(self, n: int) -> None:
        self.current = n

    def __iter__(self):  # 返回迭代器：for 会先调它
        return self

    def __next__(self) -> int:  # 每次 for 取一个值就调它一次
        if self.current <= 0:
            raise StopIteration  # 结束信号：没有更多了
        result = self.current
        self.current -= 1
        return result


for x in Countdown(3):
    print(x)  # 3 / 2 / 1
print("-----")

# 手动用也 OK：
c = iter(Countdown(2))
print(next(c))  # 2
print(next(c))  # 1
print("-----")


# ---------- 4. 生成器函数：用 yield 偷懒写迭代器 ----------
# 手写 __iter__/__next__ 啰嗦。可以用 yield 关键字的更短写法：
# 一个函数里只要出现 yield，它就不是普通函数，而是"生成器函数"。
# 调用它不跑函数体，而是返回一个生成器；每 next 一次就执行到下一个 yield。
def countdown_gen(n: int):
    while n > 0:
        yield n  # 到这里暂停，把 n 交给外面；下次 next 从这继续
        n -= 1


for x in countdown_gen(3):
    print(x)  # 3 / 2 / 1（效果和上面的类一样，代码少多了）
print("-----")


# ---------- 5. 惰性：不一次算完，内存省；还能表示无穷序列 ----------
# 普通函数 return 是一口气算完再返回；yield 是"要一个给一个"。
# 好处 1：省内存。算 10 亿个数，别先算完存列表，生成器边用边算。
#   big = list(range(10**9))   # 这样干会巨占内存，别试
#   for x in huge_gen():       # 生成器一次只占一个数的内存
# 好处 2：能表示"无穷"的序列，规则永远算不完但有始有终（用 break 停）。

def even_numbers():  # 生成无限个偶数
    n = 0
    while True:
        yield n
        n += 2


print("前 5 个偶数：")
count = 0
for e in even_numbers():
    print(e, end=" ")  # 0 2 4 6 8
    count += 1
    if count >= 5:
        break  # 别傻等，取够就停
print("\n-----")

# ---------- 6. 生成器表达式 + 转列表 ----------
# 长得像列表推导式，但用圆括号()，得到的是生成器，惰性求值。
squares = (x * x for x in range(5))
print(type(squares))  # <class 'generator'>
print(list(squares))  # [0, 1, 4, 9, 16]  用 list() 一口气取完转成列表
# 注意生成器也是一次性的：上面 list() 用掉后，再取就空了。
print(list(squares))  # []

# 对比：列表推导式 [ ] 一下就全部算好了；生成器表达式 ( ) 是懒的。
print("-----")


# ---------- 小结：什么时候用 ----------
# - 数据量小、要用很多次  -> 普通列表，直接 []
# - 数据量大、或只要遍历一次、或想表示无限序列 -> 生成器，用 ()
# - 需要 for 循环的自定义类 -> 实现 __iter__/__next__，或用 yield 写生成器


# ---------- 练习 ----------
# 1. 用 yield 写生成器 fib()，每调用一次 next 吐一个斐波那契数
#    （1, 1, 2, 3, 5, 8, ...），用 for + break 打印前 8 个。
#
# 2. 写生成器 only_even(nums)，接收一个列表，只 yield 其中偶数。
#    用它在 [1..10] 上打印 2 4 6 8 10。
#
# 3. 用生成器表达式一行算出 1~100 所有平方的和大 逐个求和用 sum()。
#


def fib_my():
    # f(n) = f(n-1) + f(n-2)
    # f(0) = 1, f(1) = 1
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def only_even_my(nums: list[int]):
    index: int = 0
    while index < len(nums):
        if nums[index] % 2 == 0:
            yield nums[index]
        index += 1


my_square = (x * x for x in range(1, 101))
print(sum(my_square))

print("===== 练习区（把上面 3 题写在这里，保存后运行）=====")


# 题1 示范：斐波那契生成器
def fib():
    a, b = 1, 1
    while True:
        yield a  # 先吐 a，再推进
        a, b = b, a + b


print("前 8 个斐波那契数：")
n = 0
for f in fib():
    print(f, end=" ")
    n += 1
    if n >= 8:
        break
print("\n-----")


# 题2 示范：只吐偶数
def only_even(nums):
    for x in nums:
        if x % 2 == 0:
            yield x


print(list(only_even(range(1, 11))))  # [2, 4, 6, 8, 10]
print("-----")

# 题3 示范：生成器表达式 + sum
total = sum(x * x for x in range(1, 101))  # 1²+2²+...+100²
print(total)  # 338350
print("-----")
