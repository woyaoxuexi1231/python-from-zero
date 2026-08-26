# ============================================================
# 第 18 课配套模块：calc.py
# 演示"模块里也能再 import 别的模块"，以及函数互相调用。
# ============================================================

from tools import add  # 模块之间也能互相 import


def sum_list(numbers: list[float]) -> float:
    """把列表里的数字全加起来。内部复用了 tools.add。"""
    total = 0.0
    for n in numbers:
        total = add(total, n)  # 用 tools 里的 add
    return total


def mean(numbers: list[float]) -> float:
    """求平均。空列表返回 0.0。"""
    if not numbers:
        return 0.0
    return sum_list(numbers) / len(numbers)
