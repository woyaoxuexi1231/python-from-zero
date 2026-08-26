# ============================================================
# 第 18 课配套模块：tools.py
# 这是一个"自己写的模块"。18_modules.py 会用 import 引入它。
# 模块 = 一个 .py 文件，里面装着函数 / 变量 / 类，供别的文件复用。
# ============================================================

# 模块里可以放普通变量
PI = 3.14159
AUTHOR = "study-hub"


# 模块里可以放函数
def greet(name: str) -> str:
    """打个招呼。"""
    return f"你好，{name}！（来自 tools 模块）"


def square(n: int) -> int:
    """返回平方。"""
    return n * n


def add(a: float, b: float) -> float:
    """两数相加。"""
    return a + b

def double(a: int) -> int:
    return a * 2


# 下面这个判断很关键，后面第 18 课会讲到：
# 当一个 .py 文件被「直接运行」时，__name__ 等于 "__main__"；
# 当它被「当作模块 import」时，__name__ 等于模块名（这里是 "tools"）。
# 所以这段保护代码只在"直接双击/运行 tools.py"时执行，被 import 时不执行。
if __name__ == "__main__":
    print("tools.py 被直接运行了")
    print(greet("世界"))
