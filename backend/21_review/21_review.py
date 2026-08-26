# ============================================================
# 第 21 课（复习课）：把第 18~20 课串起来大通关
# 运行方式：python 21_review/21_review.py
# ============================================================

# 这一课不教新东西。用一个小项目把最近三课串起来：
#   场景：扫一个文件夹里所有 .txt，逐行读、统计每个文件的行数与词数，
#         再把汇总结果写成 JSON 存盘。
#   三课的贡献：
#     18 模块 —— 工具函数放在 course_tools.py，用 import 借过来用，还有 __name__
#     19 生成器 —— 用 yield 惰性逐行读文件，不一次读进内存
#     20 pathlib —— 用 rglob 递归找文件、/ 拼路径、json 写盘
#
# 规则：下面 5 个函数都留了 pass，等你填。注释里只有"要求"，没有答案。
# 写完保存后运行本文件，底部会有自检测试（像第 17 课那样）告诉你每题过了没。
# 每个 题 的期望输出都写在测试用例的注释里；对不上就看 ❌ 改对应函数。
#
# 先定位置 + import 模块（第 20 课：Path(__file__)；第 18 课：from ... import ...）。
from pathlib import Path
import json
from course_tools import letter_grade, word_tokens   # 第 18 课：借模块里的函数

BASE = Path(__file__).resolve().parent


# ---------- 题 1：用 import 来的函数（第 18 课）----------
# 写 grade_report(book: dict[str, int]) -> str
# 用 course_tools 里 import 来的 letter_grade，
# 把成绩 dict 转成多行字符串，每行 "名字:分数 等级"。
#   要求：输出里必须同时包含 优秀/及格/不及格 三个词。
# 提示：for name, score in book.items() 一行行拼，用 \n 连接。
def grade_report(book: dict[str, int]) -> str:
    result: str = ""
    for k, v in book.items():
        result += f"{k}:{v} {letter_grade(v)}\n"
        pass
    return result
    pass


# ---------- 题 2：生成器逐行读（第 19 课）----------
# 写 read_nonempty(path: Path)
# 用 for line in f 惰性逐行读文件，只 yield 非空行（跳过 strip() 后为空的）。
#   要求1：用 yield，返回的是生成器对象（不能是现成 list）
#   要求2：空行不被 yield 出来
def read_nonempty(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if len(line.strip("\n")) == 0:
                continue
            yield line.strip("\n")
            pass
    pass


# ---------- 题 3：递归找文件（第 20 课）----------
# 写 find_txt(base: Path) -> list[Path]
# 用 rglob 找出 base 下所有 .txt 文件（含子目录），按文件名(.name)升序返回。
#   要求：返回 list[Path]，且排好序；子目录里的文件也要能找出来。
def find_txt(base: Path) -> list[Path]:
    return sorted(base.rglob("*.txt"), key=lambda x: len(x.name))
    pass


# ---------- 题 4：批量统计（把 2、3 合起来）----------
# 写 summarize_files(files: list[Path]) -> dict[str, dict[str, int]]
# 对每个文件，用 read_nonempty 拿到所有非空行，
# 用 word_tokens 数每行有几个词。
# 返回 {文件名: {"lines": 非空行数, "words": 总词数}}
#   要求：dict 的键用文件名(f.name)，不是完整路径。
def summarize_files(files: list[Path]) -> dict[str, dict[str, int]]:

    result: dict[str, dict[str, int]] = {}
    for file in files:

        lines_count = 0
        words_count = 0

        for e in read_nonempty(file):
            lines_count += 1
            words_count += len(word_tokens(e))
            result[file.name] = {"lines": lines_count, "words": words_count}

    return result
    pass


# ---------- 题 5：__name__ 守卫 + JSON 写盘（第 18、20 课）----------
# 写 save_summary(summary: dict, out: Path) -> None
# 用 json.dump 把 summary 写入 out（ensure_ascii=False, indent=2）。
def save_summary(summary: dict, out: Path) -> None:
    with open(out, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    pass


# ============ 测试框架（照搬第 17 课，不用改）============
def run_tests(title: str, cases: list[tuple]) -> bool:
    """cases: [(期望值, 实际值, 说明), ...]，自动比对并打印。"""
    print(f"\n===== {title} =====")
    ok = 0
    for i, (expected, actual, desc) in enumerate(cases, 1):
        def norm(v):
            if isinstance(v, set):
                return sorted(v)
            if isinstance(v, list) and v and isinstance(v[0], (tuple, list)):
                return sorted(v)
            return v
        passed = norm(expected) == norm(actual)
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
    # 1) 先在本课目录造示例数据（.tmp.txt / summary.tmp.json 会被 .gitignore 忽略）
    demo = BASE / "demo_data"
    demo.mkdir(exist_ok=True)
    a = demo / "a.tmp.txt"
    a.write_text("小明 90\n小红 40\n\nhulei 75\n", encoding="utf-8")
    b = demo / "b.tmp.txt"
    b.write_text("核心 数据\n\n\n\n最后一 行 词\n", encoding="utf-8")
    child = demo / "sub"
    child.mkdir(exist_ok=True)
    deep = child / "deep.tmp.txt"
    deep.write_text("藏起来的一行\n", encoding="utf-8")

    all_pass = True

    # 题1：grade_report —— 期望输出含三个等级 + 名字 + 分数
    rep = grade_report({"小明": 90, "小红": 40, "hulei": 75})
    all_pass &= run_tests("题1 grade_report（import 来的 letter_grade/多行拼接）", [
        ("优秀" in rep, True, "含等级 优秀"),
        ("及格" in rep, True, "含等级 及格"),
        ("不及格" in rep, True, "含等级 不及格"),
        ("小明" in rep and "90" in rep, True, "含 小明:90"),
        ("小红" in rep and "40" in rep, True, "含 小红:40"),
        ("hulei" in rep and "75" in rep, True, "含 hulei:75"),
        (rep.count("小明") + rep.count("小红") + rep.count("hulei") == 3, True, "三人各出现一次"),
    ])

    # 题2：read_nonempty —— 期望只 yield 非空行，且是生成器对象
    all_pass &= run_tests("题2 read_nonempty（yield 惰性/跳过空行）", [
        (list(read_nonempty(a)), ["小明 90", "小红 40", "hulei 75"], "跳过中间空行"),
        (list(read_nonempty(b)), ["核心 数据", "最后一 行 词"], "跳过连续空行"),
        (list(read_nonempty(deep)), ["藏起来的一行"], "单行文件"),
        (hasattr(read_nonempty(a), "__next__"), True, "是生成器对象(有__next__)"),
        ("" not in list(read_nonempty(a)), True, "结果里没有空串"),
    ])

    # 题3：find_txt —— 期望按名排序、包含子目录里的 deep
    ft = find_txt(demo)
    fnames = [f.name for f in ft] if isinstance(ft, list) else []
    all_pass &= run_tests("题3 find_txt（rglob 递归/按名排序）", [
        (fnames, ["a.tmp.txt", "b.tmp.txt", "deep.tmp.txt"], "全部 txt 且按名升序"),
        (isinstance(ft, list), True, "返回 list"),
        ("deep.tmp.txt" in fnames, True, "子目录里也能找到"),
        (len(fnames), 3, "共 3 个"),
    ])

    # 题4：summarize_files —— 期望按文件名统计行数/词数
    summary = summarize_files(ft) if isinstance(ft, list) else {}
    all_pass &= run_tests("题4 summarize_files（嵌套 dict 统计/键用文件名）", [
        ((summary or {}).get("a.tmp.txt"), {"lines": 3, "words": 6}, "a: 3行6词"),
        ((summary or {}).get("b.tmp.txt"), {"lines": 2, "words": 5}, "b: 2行5词"),
        ((summary or {}).get("deep.tmp.txt"), {"lines": 1, "words": 1}, "deep: 1行1词"),
        (set((summary or {}).keys()), {"a.tmp.txt", "b.tmp.txt", "deep.tmp.txt"}, "键是文件名"),
    ])

    # 题5：save_summary —— 期望写完能读回原文
    t5 = []
    out = BASE / "summary.tmp.json"
    try:
        sample = {"a.tmp.txt": {"lines": 3, "words": 6}}
        save_summary(sample, out)
        t5.append((sample, json.loads(out.read_text(encoding="utf-8")), "写完能读回"))
        save_summary(summary if isinstance(summary, dict) else sample, out)
        t5.append(("a.tmp.txt" in json.loads(out.read_text(encoding="utf-8")), True, "能写嵌套字典"))
    except Exception as e:
        print(f"\n===== 题5 save_summary（JSON写盘）=====\n  ❌ 抛异常: {e!r}")
        t5 = []
    all_pass &= run_tests("题5 save_summary（json.dump 写盘）", t5)

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部 5 题通过！第 18~20 课复习通关！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应函数，再跑一次。")