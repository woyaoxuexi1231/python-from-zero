# ============================================================
# 第 30 课（练习）：enum 枚举 —— 全部是新场景
# 运行方式：python 30_enum/30_enum_exercise.py
# ============================================================
from enum import Enum, IntEnum, StrEnum, auto

# 先读 30_enum.py。下面 6 题全是新场景。写完自检 ✅/❌。

# ---------- 题 1：定义订单状态枚举 ----------
# 定义 class OrderStatus(Enum)，三个成员：
#   PENDING = "pending"
#   SHIPPED = "shipped"
#   CANCELLED = "cancelled"
# 写 status_label(s: OrderStatus) -> str：
#   返回中文："待发货" / "已发货" / "已取消"
class OrderStatus(Enum):
    pass   # 填成员


def status_label(s: OrderStatus) -> str:
    pass


# ---------- 题 2：按 value 反查 ----------
# 用上题的 OrderStatus。
# 写 parse_status(raw: str) -> OrderStatus：
#   raw 是 "pending" 等 value，返回对应成员。
#   非法 value 抛 ValueError（直接用 Enum 构造即可）。
def parse_status(raw: str) -> OrderStatus:
    pass


# ---------- 题 3：列出所有 value ----------
# 写 all_status_values(cls) -> list[str]：
#   接收 OrderStatus 类，返回所有成员的 .value 列表（定义顺序）。
def all_status_values(cls) -> list:
    pass


# ---------- 题 4：IntEnum 等级比较 ----------
# 定义 class Level(IntEnum)：
#   BRONZE = 1, SILVER = 2, GOLD = 3
# 写 is_gold(level: Level) -> bool：是否 GOLD 及以上（value >= 3）。
class Level(IntEnum):
    pass


def is_gold(level: Level) -> bool:
    pass


# ---------- 题 5：StrEnum 主题色 ----------
# 定义 class Theme(StrEnum)：
#   LIGHT = "light", DARK = "dark"
# 写 build_query(theme: Theme) -> str：
#   返回 f"mode={theme}"（StrEnum 可直接当 str 拼）。
class Theme(StrEnum):
    pass


def build_query(theme: Theme) -> str:
    pass


# ---------- 题 6：综合 —— auto 优先级 + 找最高 ----------
# 定义 class Urgency(Enum)：
#   LOW / NORMAL / HIGH / CRITICAL 均用 auto()
# 写 max_urgency(items: list[Urgency]) -> Urgency：
#   返回 value 最大的那个成员（列表非空）。
class Urgency(Enum):
    pass


def max_urgency(items: list) -> Urgency:
    pass


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


if __name__ == "__main__":
    all_pass = True

    all_pass &= run_tests("题1 status_label", [
        (status_label(OrderStatus.PENDING), "待发货", "pending"),
        (status_label(OrderStatus.SHIPPED), "已发货", "shipped"),
        (status_label(OrderStatus.CANCELLED), "已取消", "cancelled"),
    ])

    all_pass &= run_tests("题2 parse_status", [
        (parse_status("pending"), OrderStatus.PENDING, "按 value 反查"),
        (parse_status("shipped"), OrderStatus.SHIPPED, "shipped"),
    ])
    try:
        parse_status("invalid")
        all_pass &= run_tests("题2 非法 value", [(True, False, "应抛 ValueError")])
    except ValueError:
        all_pass &= run_tests("题2 非法 value", [(True, True, "ValueError OK")])

    all_pass &= run_tests("题3 all_status_values", [
        (all_status_values(OrderStatus),
         ["pending", "shipped", "cancelled"],
         "全部 value 有序"),
    ])

    all_pass &= run_tests("题4 is_gold", [
        (is_gold(Level.GOLD), True, "GOLD"),
        (is_gold(Level.SILVER), False, "SILVER"),
        (is_gold(Level(3)), True, "value=3"),
    ])

    all_pass &= run_tests("题5 build_query", [
        (build_query(Theme.DARK), "mode=dark", "StrEnum 拼接"),
        (build_query(Theme.LIGHT), "mode=light", "light"),
    ])

    all_pass &= run_tests("题6 max_urgency", [
        (max_urgency([Urgency.LOW, Urgency.HIGH, Urgency.NORMAL]),
         Urgency.HIGH, "取 value 最大"),
        (max_urgency([Urgency.CRITICAL]), Urgency.CRITICAL, "单个"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！enum 可以上手用了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")
