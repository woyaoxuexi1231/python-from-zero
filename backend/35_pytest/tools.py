# 第 35 课演示用小模块：被 test_tools_demo.py 测
# 正式项目里「业务代码」和「测试」分文件；这里故意写短。

def add(a: int, b: int) -> int:
    return a + b


def greet(name: str, shout: bool = False) -> str:
    msg = f"你好，{name}"
    return msg.upper() if shout else msg


def clamp(x: int, lo: int, hi: int) -> int:
    if lo > hi:
        raise ValueError("lo 不能大于 hi")
    return max(lo, min(hi, x))
