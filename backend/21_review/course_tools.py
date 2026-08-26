# course_tools.py —— 供 21_review.py 导入的小工具模块
#
# 第 18 课复习点：这是"另一个模块"。21_review.py 想用这些函数，
# 就在它文件里用 `from course_tools import ...` 借过来。
#
# 运行方式：不要单独运行本文件，它是被 21_review.py import 的配角。
def letter_grade(score: int) -> str:
    """分数 → 等级：>=90 优秀，>=60 及格，否则不及格。"""
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"


def word_tokens(line: str) -> list[str]:
    """把一行按空白切成词列表。"""
    return line.split()


# ---------- 第 18 课的 __name__ ----------
# 直接运行本文件 vs 被 import，这里打印的值不同，用来验证你理解了 __name__。
if __name__ == "__main__":
    print("直接运行 course_tools.py：__name__ == '__main__'（这里直接运行的代码）")
else:
    print(f"[course_tools] 被 import 了：我的 __name__ = {__name__!r}")