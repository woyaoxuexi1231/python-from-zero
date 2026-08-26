# ============================================================
# 第 23 课（知识讲解）：装饰器 decorator —— @ 语法糖
# 运行方式：python 23_decorators/23_decorators.py
# 配套练习：23_decorators_exercise.py（自检，全是新场景）
# ============================================================

import time
import functools

# 痛点：想在多个函数前后加点东西（打日志、计时、校验权限），
# 又不想把同样的代码复制进每个函数体。装饰器就是干这个的。
# 【Java 对照】没有"装饰器"这种一等语法；最接近的是注解 + AOP 切面，
# 或者自己写包装。Python 把"包一层"做成了语言内置的语法糖。
print("========== 第23课 装饰器 decorator ==========\n")


# ---------- 1. 铺垫：函数是一等公民 ----------
# 函数可以当参数传进另一个函数，也可以被 return 出来。
print("【1】函数能当参数传、能被返回")
def greet(name: str) -> str:
    return f"你好，{name}"

def call_twice(f):
    return f + f   # 注意：这里拼的是字符串，不是调用；只为说明"函数可传递"

# 真正想表达的是下面这种：把函数当数据传来传去
def apply(f, v):
    return f(v)    # f 是一个函数

print(apply(greet, "小明"))   # 你好，小明 —— 把 greet 当参数传进 apply


# ---------- 2. 手写"包装器"（装饰器的笨办法） ----------
# 核心思想：写一个新函数 inner，先做包装的事，再调原来的函数。
print("\n【2】手写包装器：不动原函数，也能给它「加料」")
def log_deco(func):
    """返回一个新函数：调用它=打日志+调用原函数。"""
    def inner(name):
        print(f"[日志] 准备调用 {func.__name__}")
        result = func(name)         # 真正调原函数
        print(f"[日志] 调用结束，结果={result!r}")
        return result
    return inner

def greet2(name: str) -> str:
    return f"你好，{name}"

wrapped = log_deco(greet2)          # 手动包一层
print(wrapped("小红"))
# 原函数 greet2 没被动过，但调用 wrapped 时就带上了日志。


# ---------- 3. @ 语法糖 ----------
# Python 提供 `@装饰器` 写在函数定义上面，等价于：func = 装饰器(func)。
print("\n【3】@ 语法糖：等价于 func = 装饰器(func)")
@log_deco
def greet3(name: str) -> str:
    return f"你好，{name}"

print(greet3("hulei"))


# ---------- 4. 让包装器通用：*args, **kwargs ----------
# 上面 inner 写死了参数 (name)。不同函数参数不一样，用 *args/**kwargs 通吃。
# 【Java 对照】很像包装任意方法——参数不写死，靠"可变参数"透传。
print("\n【4】*args / **kwargs：包装器不再挑参数")
def timed(func):
    """统计被包装函数跑多久，参数随便几个都行。"""
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        cost = (time.perf_counter() - start) * 1000
        print(f"[计时] {func.__name__} 耗时 {cost:.2f} ms")
        return result
    return inner

@timed
def slow_add(a: int, b: int) -> int:
    for _ in range(1_000_000):
        pass
    return a + b

@timed
def slow_greet(name: str, *, times: int = 1) -> str:
    for _ in range(100_000):
        pass
    return (f"嗨，{name}　" * times)

print(slow_add(3, 5))                     # 8
print(slow_greet("阿泰", times=2))          # 两个参数形式都能接住


# ---------- 5. 保留原函数的信息：functools.wraps ----------
# 装饰后，函数的 __name__、__doc__ 会被 inner 盖掉（变成 'inner'）。
# 想在包装里把原函数的名字/文档抄回来，给 inner 加 @functools.wraps(func)。
print("\n【5】@functools.wraps(func)：保住原名和文档")
def bare_deco(func):
    """不保名字的装饰器。"""
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

def wraps_deco(func):
    """用 @functools.wraps 保名字的装饰器。"""
    @functools.wraps(func)          # 关键一行：把 func 的名/文档抄给 inner
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner

@bare_deco
def greet_a(name):
    """甲的文档"""
    return f"你好，{name}"

@wraps_deco
def greet_b(name):
    """乙的文档"""
    return f"你好，{name}"

print("没保名 wrap 后 __name__ =", greet_a.__name__)   # inner（丢失原名）
print("wraps 包后 __name__ =", greet_b.__name__)       # greet_b（保住了）


# ---------- 6. 装饰器也能带参数：工厂 ----------
# 想让 @repeat(3) 这种写法成立，装饰器得再包一层="工厂"：
#   @repeat(3)  →  先调 repeat(3) 得到真正的装饰器，再套到函数上。
print("\n【6】带参数的装饰器（工厂）：@repeat(3)")
def repeat(n: int):
    """工厂：返回一个"把函数连调 n 次"的装饰器。"""
    def deco(func):
        def inner(*args, **kwargs):
            outputs = []
            for _ in range(n):
                outputs.append(func(*args, **kwargs))
            return outputs
        return inner
    return deco

@repeat(3)
def say_hi(name: str) -> str:
    return f"嗨，{name}"

print(say_hi("小明"))       # ['嗨，小明', '嗨，小明', '嗨，小明']


# ---------- 7. 内置缓存装饰器：functools.lru_cache ----------
# 常见真实用法：给"重复算同样输入"的函数加缓存，用得到它的直接白送。
print("\n【7】functools.lru_cache：内置结果缓存")
@functools.lru_cache(maxsize=None)
def fib(n: int) -> int:
    return n if n < 2 else fib(n - 1) + fib(n - 2)

t0 = time.perf_counter()
print("fib(35) =", fib(35))
print(f"加缓存后：{(time.perf_counter() - t0)*1000:.1f} ms（快去试试把它去掉多慢）")


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("函数一等公民：   可当参数、可返回")
print("装饰的根本：     装饰器(func) 返回新函数 inner")
print("@语法糖：        @deco  ≡  func = deco(func)")
print("通用包装：       inner(*args, **kwargs) 透传")
print("保元信息：        @functools.wraps(func)")
print("带参数装饰器：   再包一层工厂 def deco_factory(参数)")
print("内置缓存：        @functools.lru_cache")