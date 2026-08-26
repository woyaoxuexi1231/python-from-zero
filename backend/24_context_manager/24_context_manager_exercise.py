# ============================================================
# 第 24 课（练习）：上下文管理器 with —— 全部是新场景
# 运行方式：python 24_context_manager/24_context_manager_exercise.py
# ============================================================
import contextlib          # 题2、题3 要用 @contextlib.contextmanager

# 先读 24_context_manager.py。那边讲了：with 文件 / 类写 __enter__/__exit__ /
# @contextmanager / __exit__ 返回 True 吞异常。
# 下面是 5 个讲稿里没出现的新场景，得把"进块准备、出块清理"这套自己迁移过去。

# ---------- 题 1：Phase 类上下文管理器（入/退标记，异常不吞） ----------
# 场景：想给一段代码打"开始/结束"桩，无论中间是否报错都要闭合。
# 写类 Phase：构造时传入 log(列表) 和 name(字符串)。
#   __enter__       往 log 追加 f"{name}:enter"，返回 self
#   __exit__(et,ev,tb)
#                    如果 et 为 None(没报错) → 追加 f"{name}:exit:ok"，返回 False
#                    如果 et 非 None(报错了) → 追加 f"{name}:exit:error"，返回 False
#                   （False = 不吞异常，错误照常往外抛）
class Phase:
    def __init__(self, log: list, name: str = "phase"):
        self.log = log
        self.name = name

    def __enter__(self):
        self.log.append(f"{self.name}:enter")
        return self

    def __exit__(self, et, ev, tb):
        if et is None:                          # 没报错 → 标记 ok
            self.log.append(f"{self.name}:exit:ok")
        else:                                   # 报错了 → 标记 error
            self.log.append(f"{self.name}:exit:error")
        return False                            # False = 异常不吞，照抛


# ---------- 题 2：@contextmanager 标注 label（yield + finally） ----------
# 场景：想记录"某段操作从哪开始、从哪结束"，用函数式写法(不用类)。
# 写函数 labeled(label, log)：用 @contextmanager 装饰。
#   进入(yield 前)：  log.append(f"{label}:start")
#   yield label       让 `with ... as who` 拿到 label 字符串
#   退出(用 finally)：log.append(f"{label}:end")   ← 正常和异常都要执行
@contextlib.contextmanager
def labeled(label: str, log: list):
    log.append(f"{label}:start")
    try:
        yield label
    finally:
        log.append(f"{label}:end")


# ---------- 题 3：@contextmanager 回滚（finally 恢复现场） ----------
# 场景：数据库事务——进块前把现场"存档"，出块后把这次改的全撤销。
# 写函数 guard(stack)：stack 是个 list，进入时记下它当前长度 n，
#   yield 之后（用 finally）把 `stack[n:]` 全部删掉 = 回滚本次新增。
#   yield 返回 n，方便块内知道快照长度。
@contextlib.contextmanager
def guard(stack: list):
    n = len(stack)
    try:
        yield n
    finally:
        del stack[n:]                           # 回滚：把本次新增的全部删掉


# ---------- 题 4：吞掉指定异常并记录 ----------
# 场景：某些错误"可以容忍"，但要留档；其他错误照常抛。
# 写类 IgnoreValueError：构造时传入一个 log(列表)。
#   __enter__ 返回 self
#   __exit__(et,ev,tb)：若 et 是 ValueError，
#                       往 log 追加 (et.__name__, str(ev))，返回 True(吞掉)；
#                       否则返回 False(照抛)。
class IgnoreValueError:
    def __init__(self, log: list):
        self.log = log

    def __enter__(self):
        return self

    def __exit__(self, et, ev, tb):
        if et is ValueError:
            self.log.append((et.__name__, str(ev)))
            return True                          # 吞掉，不抛出
        return False


# ---------- 题 5：模拟数据库连接（生命周期 + 吞异常） ----------
# 场景：连上就用、用完必断；哪怕块内 SQL 报错也要保证断开，并吞掉错误。
# 写类 Conn：构造传入 log(列表) 和 name(字符串)；自带 execute(sql) 已实现。
#   __enter__：往 log 追加 f"{name}:connect"，返回 self（这样 `as c` 后能打 c.execute）
#   __exit__ ：往 log 追加 f"{name}:disconnect"，永远返回 True（= 吞掉块内异常，保断开）
class Conn:
    def __init__(self, log: list, name: str):
        self.log = log
        self.name = name

    def execute(self, sql: str):
        self.log.append(f"{self.name}:exec:{sql}")

    def __enter__(self):
        self.log.append(f"{self.name}:connect")
        return self

    def __exit__(self, et, ev, tb):
        self.log.append(f"{self.name}:disconnect")
        return True                              # 只要退出，就连不上错误，异常吞掉


# ============ 测试框架（不用改）============
def run_tests(title: str, cases: list[tuple]) -> bool:
    print(f"\n===== {title} =====")
    ok = 0
    for i, (expected, actual, desc) in enumerate(cases, 1):
        passed = expected == actual
        ok += passed
        mark = "✅" if passed else "❌"
        print(f"  {mark} 用例{i:02d} {desc}")
        if not passed:
            print(f"        期望: {expected!r}")
            print(f"        实际: {actual!r}")
    total = len(cases)
    print(f"  ---> {title}: {ok}/{total} 通过")
    return ok == total


def raises(fn, exc=Exception):
    """辅助：fn 抛 exc 类异常则返回 True，否则 False。"""
    try:
        fn()
    except exc:
        return True
    except Exception:
        return False
    return False


if __name__ == "__main__":
    all_pass = True

    # ---- 题1：正常走一遍 ----
    log1 = []
    def run_ok():
        with Phase(log1, "A"):
            log1.append("body")
    run_ok()
    all_pass &= run_tests("题1a Phase 正常进入/退出", [
        (log1, ["A:enter", "body", "A:exit:ok"], "进→块→正常退，成对"),
    ])
    # ---- 题1：中途报错 ----
    log2 = []
    def run_err():
        with Phase(log2, "B"):
            log2.append("before-err")
            raise ValueError("boom")
    all_pass &= run_tests("题1b Phase 异常也闭合且不吞", [
        (raises(lambda: run_err(), ValueError), True, "错误被重新抛出"),
        (log2, ["B:enter", "before-err", "B:exit:error"], "异常退出也留了桩"),
    ])

    # ---- 题2：正常 ----
    log_l = []
    with labeled("task", log_l) as who:
        got = who
    all_pass &= run_tests("题2a labeled 正常", [
        (got, "task", "as 能拿到 yield 出来的 label"),
        (log_l, ["task:start", "task:end"], "start 进 / end 出"),
    ])
    # ---- 题2：异常也闭环 ----
    log_l2 = []
    def boom2():
        with labeled("p", log_l2):
            raise ValueError("x")
    all_pass &= run_tests("题2b labeled 异常也 end", [
        (raises(lambda: boom2(), ValueError), True, "异常照抛"),
        (log_l2, ["p:start", "p:end"], "finally 保证 end 被写"),
    ])

    # ---- 题3：正常回滚 ----
    stack = [1, "a"]
    with guard(stack) as snap:
        stack.append("临时1")
        stack.append("临时2")
    all_pass &= run_tests("题3a guard 正常回滚", [
        (stack, [1, "a"], "本次新增被回滚(现场恢复)"),
        (snap, 2, "yield 返回快照长度(进入前长度)"),
    ])
    # ---- 题3：return 提前退出照样回滚 ----
    stack9 = [9]
    def early():
        with guard(stack9):
            stack9.append(99)
            return "早退"
    early()
    all_pass &= run_tests("题3b guard return 早退也回滚", [
        (stack9, [9], "return 提前走，finally 也把新增清掉"),
    ])

    # ---- 题4：吞掉 ValueError 并记录 ----
    cap = []
    def bad():
        with IgnoreValueError(cap):
            raise ValueError("bad thing")
    bad()   # 不抛
    other = []
    def oops():
        with IgnoreValueError(other):
            raise TypeError("别的错")
    all_pass &= run_tests("题4 IgnoreValueError", [
        (cap, [("ValueError", "bad thing")], "ValueError 被吞且留档"),
        (raises(lambda: oops(), TypeError), True, "其余错误照抛"),
        (other, [], "非 ValueError 不记录"),
    ])

    # ---- 题5：连接生命周期 ----
    log_c = []
    with Conn(log_c, "db") as c:
        c.execute("SELECT 1")
        c.execute("SELECT 2")
    all_pass &= run_tests("题5a Conn 生命周期", [
        (log_c, ["db:connect", "db:exec:SELECT 1", "db:exec:SELECT 2", "db:disconnect"],
         "连接→两查→断开，as 后能用 execute"),
    ])
    # ---- 题5：块内抛 SQL 错，也要断开且吞掉 ----
    logc2 = []
    def sql_fail():
        with Conn(logc2, "db2"):
            raise RuntimeError("sql死球")
    sql_fail()   # 被 __exit__ 吞掉，不抛
    all_pass &= run_tests("题5b Conn 错误也断开", [
        (logc2, ["db2:connect", "db2:disconnect"], "异常时依然 connect→disconnect 配对"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！with 的进/退/回滚/吞异常都掌握了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")