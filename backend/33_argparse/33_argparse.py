# ============================================================
# 第 33 课（知识讲解）：argparse —— 把菜单升级成命令行工具
# 运行方式：python 33_argparse/33_argparse.py
# 配套练习：33_argparse_exercise.py（自检，全是新场景）
# ============================================================
import argparse

# 痛点：第 7 课 while 菜单适合交互；脚本常要「一条命令跑完」：
#   python tool.py Alice --times 3
# 手拆 sys.argv 又脆又难写 --help。argparse 帮你声明参数、类型、默认值、帮助信息。
# 演示里一律 parse_args([...]) 传入列表，不碰真实命令行，方便对照输出。
print("========== 第33课 argparse ==========\n")


# ---------- 1. 最小例子：位置参数 ----------
print("【1】位置参数：必须按顺序给")

# ArgumentParser：创建一个"参数解析器"对象，赋值给变量 p
# description 参数：给这个解析器写一句描述，运行 python xxx.py -h 时会显示
# 比如这里 description="打招呼"，意思是"这是一个打招呼的配置"
p = argparse.ArgumentParser(description="打招呼（这是一个问候工具的配置）")

# add_argument：声明这个脚本需要哪些参数
# "name" 是位置参数（没有 - 前缀），必须按顺序提供
p.add_argument("name", help="要问候的人")

# parse_args：解析传入的参数列表，返回一个 Namespace 对象
# 传入的是一个 list（列表），列表里的每个值按顺序对应前面 add_argument 声明的位置参数
# 这里只有一个位置参数 name，所以列表第一个元素 "hulei" 就赋值给 args.name
# 如果有多个位置参数，比如声明了 src、dst 两个，那就要传 ["a.txt", "b.txt"]，按顺序一一对应
args = p.parse_args(["hulei"])          # 模拟命令行：python xxx.py hulei
print("  args.name =", args.name)       # hulei
print("  类型:", type(args))            # Namespace（argparse 返回的专用容器，用 .属性名 取值）


# ---------- 2. 可选参数：--xxx / -x ----------
print("\n【2】可选参数：有默认值，可省略")
p = argparse.ArgumentParser()
p.add_argument("name")   # 位置参数：没有 - 前缀，按顺序给，必填

# 可选参数：必须以 -（短选项）或 --（长选项）开头
# - 短选项：通常一个字母，如 -v、-t
# -- 长选项：完整单词，如 --times、--output
# type=int：自动把这个参数的值转成整数
# default=1：如果不传这个参数，默认值就是 1
p.add_argument("--times", type=int, default=1, help="重复次数")

# 只传位置参数 name="小明"，没传 --times，所以用默认值 1
print("  默认:", p.parse_args(["小明"]))

# 列表里：--times 和 "3" 是成对出现的，"3" 紧跟在 --times 后面就是它的值
# ["小明", "--times", "3"]  →  name="小明", times=3
print("  指定:", p.parse_args(["小明", "--times", "3"]))

# 短选项写法：可以同时指定短选项和长选项
# p.add_argument("-t", "--times", type=int, default=1)
# 这样命令行里 python xxx.py 小明 -t 3 和 python xxx.py 小明 --times 3 都可以


# ---------- 3. 开关：store_true / store_false ----------
print("\n【3】开关：出现即 True")
p = argparse.ArgumentParser()
p.add_argument("--verbose", "-v", action="store_true", help="详细输出")
print("  无开关:", p.parse_args([]).verbose)            # False
print("  有开关:", p.parse_args(["-v"]).verbose)        # True


# ---------- 4. choices：限制取值 ----------
print("\n【4】choices：只能是给定集合")
p = argparse.ArgumentParser()
p.add_argument("--mode", choices=["fast", "safe"], default="safe")
print("  合法:", p.parse_args(["--mode", "fast"]).mode)
# p.parse_args(["--mode", "slow"]) 会打印错误并 SystemExit——别在演示里硬跑


# ---------- 5. 多个位置参数 + 类型 ----------
print("\n【5】多位置参数与 type=")
p = argparse.ArgumentParser()
# 声明了两个位置参数：先 src，再 dst
p.add_argument("src")
p.add_argument("dst")
p.add_argument("--count", type=int, default=1)  # 可选参数，--xxx 形式
# parse_args 传入的是 list：列表前两个元素按顺序对应 src、dst
# "a.txt" → src, "b.txt" → dst, "--count", "2" → count=2
ns = p.parse_args(["a.txt", "b.txt", "--count", "2"])
print("  src/dst/count:", ns.src, ns.dst, ns.count)


# ---------- 6. 常用骨架：build_parser + main ----------
print("\n【6】推荐骨架（真实脚本怎么写）")


def build_greet_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="命令行打招呼")
    parser.add_argument("name", help="名字")
    parser.add_argument("--times", type=int, default=1, help="次数")
    parser.add_argument("-v", "--verbose", action="store_true")
    return parser


def greet_main(argv: list[str] | None = None) -> str:
    """argv=None 时读真实 sys.argv；测试时传入列表。"""
    args = build_greet_parser().parse_args(argv)
    line = f"你好，{args.name}"
    if args.verbose:
        line += f"（重复 {args.times} 次）"
    return "\n".join([line] * args.times)


print(greet_main(["Alice", "--times", "2", "-v"]))


# ---------- 7. 易错点 ----------
print("\n【7】易错点速记")
print("  ① 位置参数没有 --，顺序固定；可选参数以 -/-- 开头")
print("  ② type=int 写在 add_argument 里，不要自己再 int(args.times)")
print("  ③ action='store_true' 默认是 False；出现开关才变 True")
print("  ④ 测试/演示用 parse_args(['a','--x','1'])，别依赖真实命令行")
print("  ⑤ 非法参数会 SystemExit——练习里用合法 argv；正式工具靠 -h 看帮助")
print("  ⑥ 参数名 --out-file 在 Namespace 里变成 out_file（横杠→下划线）")


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("ArgumentParser()                 —— 建解析器")
print("add_argument('name')              —— 位置参数（必填）")
print("add_argument('--n', type=int, default=1)  —— 可选+类型+默认")
print("add_argument('-v', action='store_true')   —— 开关")
print("add_argument('--m', choices=[...])        —— 限定取值")
print("parse_args(argv) → Namespace      —— 用 args.xxx 取值")
print("python tool.py -h                 —— 自动生成帮助")
