# ============================================================
# 第 32 课（知识讲解）：re 正则 —— 从文本里抠字段
# 运行方式：python 32_re/32_re.py
# 配套练习：32_re_exercise.py（自检，全是新场景）
# ============================================================
import re

# 痛点：日志里抓日期、抓邮箱、抓手机号、删多余空格——用字符串切片硬扣又慢又脆。
# 正则：用一小段「模式」描述「长什么样」，用函数去搜、找、替换、切。
# 先用最常用的四个：search / findall / fullmatch / sub。`match` 只在开头，用得少。
print("========== 第32课 re 正则 ==========\n")


# ---------- 1. 最简单：数字 ----------
print("【1】\\d 单个数字")
text = "我的id是 7 号"
m = re.search(r"\d", text)        # 第一次出现数字
print("  search:", m.group())     # 7
print("  位置:", m.start(), m.end())


# ---------- 2. 量词：+ 一个或多个，* 零或多个 ----------
print("\n【2】\\d+ 一个以上的数字")
text = "订单号 abc-20260824-9"
for m in re.finditer(r"\d+", text):      # finditer 逐个找
    print("  找到:", m.group(), "在", text[m.start():m.end()])


# ---------- 3. findall：把全部匹配的片段拿回来 ----------
print("\n【3】findall：一次拿全部")
text = "电话 13812345678，座机 010-88889999"
print("  全部数字段:", re.findall(r"\d+", text))


# ---------- 4. 字符类与分组 ----------
print("\n【4】[...] 字符类、( ) 分组")
text = "abc123def456"
m = re.search(r"([a-z]+)(\d+)", text)    # 字母段 + 数字段
print("  整个匹配:", m.group(0))
print("  组1(字母):", m.group(1), "| 组2(数字):", m.group(2))
# findall 里有分组时，返回元组组成的列表
print("  findall:", re.findall(r"([a-z]+)(\d+)", text))


# ---------- 5. 常用速记：\d数字 \w字母数字 \s空白 ----------
print("\n【5】\\w、\\s 与数量")
text = "hello world 123 ok"
print("  字母数字段:", re.findall(r"\w+", text))
print("  空白位置数:", len(re.findall(r"\s", text)))


# ---------- 6. fullmatch：整段完全匹配（校验最常用） ----------
print("\n【6】fullmatch：必须从头到脚完全对上")
email_ok = "abc@example.com"
email_bad = "not-an-email!"
pat = r"[a-z]+@[a-z]+\.[a-z]+"
print("  email 校验:", bool(re.fullmatch(pat, email_ok)))    # True
print("  email 校验:", bool(re.fullmatch(pat, email_bad)))   # False


# ---------- 7. sub：替换 ----------
print("\n【7】sub 替换")
text = "今天 2026-08-24 明天 2026-08-25"
print("  全替换:", re.sub(r"\d+", "#", text))
# 用分组反向引用：把 MM-DD 年份不动日期格式换
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
print("  年月日分别取出:", m.group(1), m.group(2), m.group(3))


# ---------- 8. 易错点 ----------
print("\n【8】易错点速记")
print("  ① 字符串前加 r：r\"\\d+\" 让反斜杠按字面，别吃转义")
print("  ② \\d+ 贪婪会尽量多吃；要最小用 \\d+? 或不纠结")
print("  ③ search 找第一个；findall 全找（有分组回元组）；fullmatch 整段")
print("  ④ 校验输入优先 fullmatch，别用 search（会只匹配中间一段漏了前后非法）")
print("  ⑤ 正则上手先背：\\d \\w \\s + * [ ] ( ) 这 8 个就够")
print("  ⑥ 复杂正则难读：拆成小段分组命名(?P<name>...) 更清晰")


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("re.search(p, s).group()    —— 第一个匹配")
print("re.findall(p, s)           —— 全部匹配（有分组→元组列表）")
print("re.fullmatch(p, s)         —— 整段校验（返回 None/match）")
print("re.sub(p, rep, s)          —— 替换")
print("\\d数字 \\w字母数字 \\s空白  +一个以上 *零个以上 [..]集合 (..)分组")
print("raw 字符串 r\"...\" 别忘了")