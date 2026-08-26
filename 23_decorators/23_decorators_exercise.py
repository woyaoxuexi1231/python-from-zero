# ============================================================
# 第 23 课（练习）：装饰器 decorator —— 全部是新场景
# 运行方式：python 23_decorators/23_decorators_exercise.py
# ============================================================


# 先读 23_decorators.py 学概念（那里只讲了 日志/计时/重复/缓存 几个例子）。
# 下面 5 题是"旧知识、新战场"：场景都是讲稿里没有的，别想抄，
# 得把"包装函数 + 透传 *args/**kwargs"这个套路自己迁移过去。
# 规则不变：只给要求 + 骨架(pass)，不预置答案；写完自检 ✅/❌。

# ---------- 题 1：重试装饰器（工厂） ----------
# 场景：调接口经常抖，失败想自动重试几次。
# 写装饰器工厂 retry(times)：调用目标函数时，若抛异常，最多额外重试 times 次；
# 若最终还失败，就抛出最后一次的异常。
#   提示：要套用 @retry(2)，retry 要 return 一个"真正的装饰器"
#        真正的装饰器再 return 一个 inner，inner 里用 for 试 times+1 次。
def retry(times: int):
    def deco(func):
        def inner(*args, **kwargs):
            last = None
            for _ in range(times + 1):       # 首次 + 额外重试 times 次
                try:
                    return func(*args, **kwargs)   # 成功直接返回
                except Exception as e:
                    last = e                       # 记下这次失败
            raise last                             # 全败抛最后一次异常
        return inner
    return deco


# ---------- 题 2：参数校验装饰器 ----------
# 场景：有些函数不允许负数入参。
# 写装饰器 non_negative：包装的函数如果收到的参数里有负数，直接抛 ValueError，
# 否则正常执行并返回结果。
#   提示：用 *args 遍历每个位置参数，遇到 < 0 就 raise。
def non_negative(func):
    def inner(*args, **kwargs):
        for arg in args:                 # 校验每个位置参数
            if arg < 0:
                raise ValueError(f"参数不能为负数: {arg}")
        return func(*args, **kwargs)     # 校验通过才执行，并返回结果
    return inner


# ---------- 题 3：权限守卫装饰器 ----------
# 场景：管理后台，只有 admin 能删数据。
# 写装饰器 admin_only：执行前检查全局变量 current_user，若不等于 "admin"
# 就抛 PermissionError；等于才执行原函数并返回结果。
#   （current_user 由下面 set_current() 修改，你只需在里面读它）
current_user = "guest"


def set_current(name: str) -> None:
    global current_user
    current_user = name


def admin_only(func):
    def inner(*args, **kwargs):
        if current_user != "admin":      # 非 admin 拒绝
            raise PermissionError("需要 admin 权限")
        return func(*args, **kwargs)     # 通过才执行并返回
    return inner


# ---------- 题 4：调用计数装饰器 ----------
# 场景：想知道某个函数被调了多少次。
# 写装饰器 counted：让包装出来的新函数自带一个 call_count 属性（从 0 开始），
# 每被调用一次就 +1，并且仍要返回原函数的结果。
#   提示：inner = 普通函数，可以在函数体里 inner.call_count 这种加属性。
def counted(func):
    def inner(*args, **kwargs):
        inner.call_count += 1            # 每调一次 +1
        return func(*args, **kwargs)     # 并正常返回结果
    inner.call_count = 0                 # 初值挂 0，随包装函数走
    return inner


# ---------- 题 5：兜底值装饰器（工厂） ----------
# 场景：dict.get() 查不到返回 None，想要"查不到就给默认值"。
# 写装饰器工厂 fallback(default)：若被包装函数返回 None，就改成返回 default，
# 否则原样返回。
#   提示：和题 1 一样是两层（工厂 + 装饰器）。
def fallback(default):
    def deco(func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)      # 注意是 **kwargs，不是 *kwargs
            return default if result is None else result
        return inner
    return deco


# ============ 测试框架（照搬，不用改）============
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

    # ---- 题1 消费者：前两次抛，重试后成功 ----
    calls1 = []


    @retry(times=2)
    def flaky(x):
        calls1.append(x)
        if len(calls1) < 2:
            raise ValueError("临时失败")
        return f"ok-{x}"


    all_pass &= run_tests("题1 重试装饰器（工厂 @retry(times)）", [
        (flaky(5), "ok-5", "前两次失败后第3次成功"),
        (calls1 == [5, 5], True, "确实重试了一次(共调2次)"),
    ])

    # ---- 题1 消费者：始终失败，重试耗尽后抛最后一次异常 ----
    calls_b = []


    @retry(times=1)
    def boom_b():
        calls_b.append(1)
        raise RuntimeError("x")


    all_pass &= run_tests("题1b 重试耗尽 | 次数边界", [
        (raises(lambda: boom_b()), True, "@retry(1) 最后仍抛异常"),
        (calls_b == [1, 1], True, "共尝试 times+1=2 次"),
        (raises(lambda: boom_b()), True, "每次都抛、不复用上次结果"),
    ])


    # ---- 题2 消费者：除法 ----
    @non_negative
    def div(a, b):
        return a / b


    all_pass &= run_tests("题2 参数校验装饰器 @non_negative", [
        (div(10, 2), 5.0, "正常入参照常算"),
        (div(9, 3), 3.0, "结果能透传"),
        (raises(lambda: div(10, -2), ValueError), True, "负的除数被拦"),
        (raises(lambda: div(-1, 5), ValueError), True, "负的被除数被拦"),
    ])


    # ---- 题3 消费者：删数据 ----
    @admin_only
    def delete_data():
        return "已删除"


    set_current("admin")
    all_pass &= run_tests("题3b 管理员可执行", [
        (delete_data(), "已删除", "admin 能删"),
    ])
    set_current("tom")
    all_pass &= run_tests("题3c 非管理员被拦", [
        (raises(lambda: delete_data(), PermissionError), True, "普通用户触犯权限被拦"),
    ])


    # ---- 题4 消费者：打招呼 ----
    @counted
    def hello(name="world"):
        return f"hi {name}"


    hello()
    hello("a")
    all_pass &= run_tests("题4 调用计数装饰器 @counted", [
        (hello.call_count, 2, "已调用2次"),
        (hello("b"), "hi b", "结果正常返回"),
        (hello.call_count, 3, "再调1次变3"),
        (hasattr(hello, "call_count"), True, "新函数自带 call_count 属性"),
    ])


    # ---- 题5 消费者：dict.get 兜底 ----
    @fallback("查无此项")
    def find(key, data):
        return data.get(key)


    all_pass &= run_tests("题5 兜底值装饰器（工厂 @fallback(default)）", [
        (find("a", {"a": 1}), 1, "有值原样返回"),
        (find("x", {"a": 1}), "查无此项", "None 被换成默认值"),
        (find("z", {}), "查无此项", "空 dict 也兜底"),
        (find("ok", {"ok": 0}), 0, "值为0不误判(None才兜底)"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！5 个新场景都吃下了，装饰器这关过关！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应装饰器，再跑一次。")
