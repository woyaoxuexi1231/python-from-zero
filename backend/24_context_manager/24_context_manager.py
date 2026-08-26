# ============================================================
# 第 24 课（知识讲解）：上下文管理器 with —— 用完自动清理
# 运行方式：python 24_context_manager/24_context_manager.py
# 配套练习：24_context_manager_exercise.py（自检，全是新场景）
# ============================================================
import time

# 痛点：开资源(文件/锁/连接/事务)用完必须关。忘关 = 泄漏。
# with 就是"进块时准备，出块时保证清理"的语法。
# 【Java 对照】≈ try-with-resources：
#     try (var f = new BufferedReader(...)) { ... }  自动 close()
# Python 用 with，连 close 都不用写。
print("========== 第24课 上下文管理器 with ==========\n")


# ---------- 1. 先看最常用的用法：with 文件 ----------
print("【1】with 文件：进了自动开，出来自动关")
with open("24_context_manager/hello.txt", "w", encoding="utf-8") as f:
    f.write("第 24 课，你好！\n")
# 到这里 f 已经被自动关闭了（不用写 f.close()）
print("写完了，文件已自动关闭。访问一个已关闭的文件：")
try:
    with open("24_context_manager/hello.txt", "r", encoding="utf-8") as f:
        print(f.read().strip())
    print("读到内容了，再次自动关闭。")
except Exception as e:
    print("  报错：", e)


# ---------- 2. with 到底帮你做了什么 ----------
# with 的本质：进入时调用 __enter__（准备/拿资源），
#             无论块内是否抛异常，退出时都调用 __exit__（清理）。
# 语法：
#   with 上下文管理器 as 变量:
#       ...块内语句...
# 退出块(正常结束 OR 抛异常) 都会走 __exit__，保证清理。
print("\n【2】with 的原理：__enter__ / __exit__")
print("  with X as v:  ===  v = X.__enter__() 进块  ===  X.__exit__() 出块")


# ---------- 3. 自己写一个上下文管理器（类方式） ----------
# 想控制"资源准备/清理"，就实现 __enter__ 和 __exit__。
class Timer:
    """计时:进入开始计时，退出打印耗时(即使中途报错也会触发)。"""
    def __init__(self, label: str = "步骤"):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self                 # as 后拿到的就是它

    def __exit__(self, exc_type, exc_val, exc_tb):
        cost = (time.perf_counter() - self.start) * 1000
        print(f"  [{self.label}] 耗时 {cost:.2f} ms（离开时自动触发）")
        return False                # 返回 False = 异常不吞掉，照常往外抛

print("\n【3】手写上下文管理器：with Timer() as t:")
with Timer("循环 50 万次"):
    total = 0
    for i in range(500_000):
        total += i
print("  块正常结束，上面那句耗时来自 __exit__ 自动调用。")


# ---------- 4. __exit__ 的异常处理三件套 ----------
# __exit__(exc_type, exc_val, exc_tb)：块里若抛异常，这三个会被传进来。
#   返回 True  = 把这个异常"吞掉"不往外抛；返回 False/None = 照常抛出。
class SuppressZeroDivision:
    """吞掉除零错误，其他错误照抛。"""
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is ZeroDivisionError   # 只有除零被吞

print("\n【4】__exit__ 决定异常吞不吞")
try:
    with SuppressZeroDivision():
        n = 1 / 0
    print("  除零被吞掉了，没抛出来 ✅")
except ZeroDivisionError:
    print("  除零抛出来了 ❌")

try:
    with SuppressZeroDivision():
        raise ValueError("其他错误")
except ValueError as e:
    print(f"  其他错误照常抛出 ✅: {e}")


# ---------- 5. 更方便的写法：contextlib.contextmanager ----------
# 不想写类？用 @contextmanager 装饰"生成器"函数即可：yield 前=进入，yield 后=退出。
import contextlib

@contextlib.contextmanager
def opened(path: str, mode: str = "r"):
    print(f"  [进入] 打开 {path}")
    f = open(path, mode, encoding="utf-8")
    try:
        yield f                  # 这里交出控制：with ... as f 拿到的是 f
    finally:
        f.close()                # 不管块内如何，都执行关闭
        print(f"  [退出] 关闭 {path}")

print("\n【5】@contextmanager 写法")
with opened("24_context_manager/hello.txt", "r") as f:
    print("  块内读到：", f.read().strip())
# 顺序：进入 → 块内 → 退出(关闭)


# ---------- 6. 块里不用 as：只图"自动清理" ----------
class FakeLock:
    def __enter__(self):
        print("   [锁] 加锁")
        return self
    def __exit__(self, *a):
        print("   [锁] 释放(无异常也会)")


def use_lock():
    with FakeLock():
        return "  业务代码跑完了"
    # 另一种：即使 return 提前退出，__exit__ 依然会跑

print("\n【6】return 提前退出，__exit__ 照样执行")
print(use_lock())


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("with X as v / without as：  进出块式资源管理")
print("__enter__：进块准备，返回值给 as")
print("__exit__(type,val,tb)：出块清理，返回 True 吞异常")
print("@contextmanager：yield 前=进入，finally=退出")
print("最常用场景：文件、锁、数据库连接、事务、计时")