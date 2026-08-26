# ============================================================
# 第 20 课：文件与路径实操（pathlib / os / 目录遍历 / 惰性读大文件）
# 运行方式：python 20_files_paths/20_files_paths.py
# ============================================================


# 第 9 课学过：open() / with / json 读写单个文件，用的是相对路径。
# 这一课解决三个新问题：
#   1. 拼路径 / 拆路径：不同系统反斜杠还是斜杠？用字符串 + 老出 bug → pathlib
#   2. 遍历一个目录、批量处理一堆文件 → iterdir / glob / rglob
#   3. 大文件别 f.read() 一口气读进内存 → 逐行读，还能用第 19 课的生成器
#
# 你写 Java：有 java.nio.file.Path / Files.walk / 逐行 BufferedReader。
# Python 的 pathlib.Path 更顺手：路径就是对象，用 / 直接拼接，跨平台。
#
# 先记住一句话：Python 3.6+ 推荐用 pathlib 操作路径，别再用字符串拼。


# ---------- 0. 定位本文件目录（这本身就是一个 pathlib 实用点）----------
# __file__ 是"当前这个 .py 的路径"。它的父目录就是本课文件夹。
# 用 resolve() 转成绝对路径，.parent 取上一级。这样无论你在哪跑，都找得到配套文件。
from pathlib import Path

BASE = Path(__file__).resolve().parent
print("本课文件夹 BASE =", BASE)
print("文件扩展名     =", BASE.suffix)          # ''（文件夹没有后缀）
print("-----")


# ---------- 1. pathlib.Path：路径是对象，用 / 拼 ----------
# 别再写 "data" + "/" + "a.txt" 或用逗号拼字符串。用 / 直接连，自动处理系统分隔符。
demo = BASE / "demo_data"            # 在本课文件夹下造一个数据目录
print("目标目录 =", demo)
print("是否存在 =", demo.exists())    # 现在是 False，下面第 2 节会建它

# 常用属性
p = BASE / "20_files_paths.py"
print("name   =", p.name)        # 20_files_paths.py（最后一层名字）
print("stem   =", p.stem)        # 20_files_paths（去掉后缀的文件名）
print("suffix =", p.suffix)      # .py（文件类型）
print("parent =", p.parent)      # BASE
print("绝对?  =", p.is_absolute())  # Path(__file__) 本来就是绝对路径
print("-----")


# ---------- 2. 本课自建几个示例文件（分类型，方便演示过滤）----------
# .tmp.txt 会被 from-zero/.gitignore 里的 *.tmp.* 规则忽略，不会污染 git。
demo.mkdir(exist_ok=True)          # 目录不存在就建；存在也不报错

(demo / "note1.tmp.txt").write_text("小明 90\n小红 40\nhulei 75\n", encoding="utf-8")
(demo / "note2.tmp.txt").write_text("第一行\n第二行\n", encoding="utf-8")
(demo / "readme.tmp.md").write_text("# 这是一个 markdown\n并不是文本统计目标\n", encoding="utf-8")
(demo / "config.tmp.json").write_text('{"mode": "demo"}\n', encoding="utf-8")

# 之后每次运行，上面会重新写一遍这 4 个文件（幂等，无副作用）。
print("已在本课目录生成 demo_data：")
for f in demo.iterdir():            # iterdir：列出目录里的一层
    print("  ", f.name)
print("-----")


# ---------- 3. 遍历目录：iterdir（一层） / glob（按规则匹配）----------
print("demo_data 里的 .txt 文件（glob）：")
for f in demo.glob("*.txt"):
    print("  ", f.name)             # 只匹配后缀 .txt 的
# note1.tmp.txt / note2.tmp.txt

print("demo_data 里所有文件（iterdir）：")
for f in demo.iterdir():
    print("  ", f.name)

# glob 支持通配符，和命令行很像：*.txt、*_2.*、[a-z]* ...
print("-----")


# ---------- 4. 子目录也能找：rglob（递归） / os.walk ----------
# iterdir / glob 都只看当前目录一层。要钻进子目录，用 rglob。
# 先建一个带子目录的结构感受一下：
child = demo / "sub"
child.mkdir(exist_ok=True)
(child / "deep.tmp.txt").write_text("藏在子目录里\n", encoding="utf-8")

print("rglob 递归找所有 .txt：")
for f in demo.rglob("*.txt"):
    print("  ", f.name)             # 包括 sub/deep.tmp.txt

# os.walk 是更传统的递归遍历，写起来啰嗦，一般 rglob 就够大多数场景了。
import os
print("os.walk 结果（目录, 子目录列表, 文件列表）：")
for root, dirs, files in os.walk(demo):
    print("  目录:", os.path.basename(root), "文件:", files)
print("-----")


# ---------- 5. 惰性读大文件：逐行读，别 f.read() 一口气喝干 ----------
# 如果文件有几 GB，`f.read()` 会把整个文件装进内存，直接就爆了。
# 正确做法：用 for 读一行处理一行；再包成生成器（接第 19 课）随用随给。
def read_lines(path: Path):
    """生成器：逐行 yield，读完一行就释放一行，不占内存。"""
    with open(path, encoding="utf-8") as f:
        for line in f:              # 这里的 for 本身就是逐行读（惰性）
            yield line.rstrip("\n") # 去掉行尾换行再交出去


print("用生成器逐行读 note1.tmp.txt：")
for line in read_lines(demo / "note1.tmp.txt"):
    print("  读到:", line)
# 读到: 小明 90 / 读到: 小红 40 / 读到: hulei 75
print("-----")


# ---------- 6. 实战：批量统计一个目录里所有 .txt ----------
# 把 3、5 结合：遍历 → 对每个文件逐行处理 → 汇总写 JSON（接第 9 课）。
import json

summary: dict[str, dict[str, int]] = {}
for f in demo.glob("*.txt"):  # 只挑文本
    lines = list(read_lines(f))      # 一口气取完（文件小，无所谓）
    words = sum(len(l.split()) for l in lines)   # 空行 split 后为空，不加数
    summary[f.name] = {"lines": len(lines), "words": words}

print("统计结果：")
print(json.dumps(summary, ensure_ascii=False, indent=2))
# 预期：note1=3 行6 词、note2=2 行2 词、deep=1 行1 词

out = BASE / "summary.tmp.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print("已写入：", out)
print("-----")


# ---------- 7. 防御：文件/目录不存在 ----------
# 读文件前先 exists() 判断，或直接 try/except 接住（第 8 课）。
missing = BASE / "demo_data" / "不存在的.tmp.txt"
if missing.exists():
    print("存在！")
else:
    print("文件不存在，先建/跳过。")

# 也可以用 Path.exist 之外的方式：直接读，让它抛 FileNotFoundError 再接住。
try:
    text = missing.read_text(encoding="utf-8")
except FileNotFoundError:
    print("用 try/except 也接住了：文件不存在了。")
print("-----")


# ---------- 小结 ----------
# - 路径用 pathlib.Path，/ 拼接、.name/.parent/.suffix 拆、.exists() 判断
# - 遍历一个目录：iterdir(一层) / glob("*.txt") / rglob(递归)
# - 大文件：for 逐行 / 生成器，别 read() 一次全载
# - 批量处理 = 遍历 + 逐文件处理 + 汇总（可以再写回 JSON）
#
# 提示：Path("a") / "b" / "c.py" 返回的是新 Path，别把字符串混进去拼。


# ---------- 练习 ----------
# 1. 用 pathlib 打印 20_files_paths.py 的文件名、大小（用 .stat().st_size）,
#    并以"KB"为单位打印（bytes / 1024）。
#



print("===== 练习区域 =====")

import pathlib
path = pathlib.Path(__file__)

print(f"file name : {path.name}")
print(f"Path : {path}")
print(f"file size : {path.stat().st_size} bytes")
print(f"file size : {path.stat().st_size / 1024} KB")



# 2. 用 rglob 找出 demo_data 里所有 .json 和 .md 文件，打印它们的绝对路径。
#

# 我们测试的位置就是当前文件的目录下的 demo_data 目录
path = (pathlib.Path(__file__).resolve()).parent

path_1 = path  / "demo_data"
path_pattern: list[str] = ["*.json","*.md"]

for e in path_pattern:
    for e_ in path_1.rglob(e):
        print(e_.resolve())



# 3. 写一个函数 word_count(path) -> int，用 read_lines 逐行统计总词数。
#    然后在 demo_data 的所有 .txt 上调它，把每个文件的词数打印出来。
#

def word_count(path_def: Path) -> int:

    # 找到所有 .txt 的文件
    total = 0
    for e in path_def.rglob("*.txt"):
        sumcount: int = 0
        for read_line in read_lines(e):
            sumcount += len(read_line.rstrip("\n").split())
            pass
        print(f"文件: {e.name} 字数: {sumcount}")
        total += sumcount
    pass


file____resolve__parent = pathlib.Path(__file__).resolve().parent
word_count(file____resolve__parent/ "demo_data")


# （本课练习答案由你自己完成，这里不再预置参考答案）