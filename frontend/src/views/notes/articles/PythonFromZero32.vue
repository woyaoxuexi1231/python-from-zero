<template>
  <div class="article">
    <p>
      日志里抓日期、抓邮箱、抓手机号、把多余空格清干净——用字符串切片硬扣又慢又脆。
      正则用一小段「模式」描述「长什么样」，一次搞定。这一课只讲最常用的四个函数和八个写法。
    </p>

    <h2>这一课解决什么问题</h2>
    <ul>
      <li>找第一个 → <code>re.search(...)</code></li>
      <li>全部匹配 → <code>re.findall(...)</code></li>
      <li>整段校验 → <code>re.fullmatch(...)</code>（输入校验优先用这个）</li>
      <li>替换 → <code>re.sub(...)</code></li>
    </ul>

    <h2>先记这八个写法</h2>
<pre><code>\d   一个数字       \w   字母或数字       \s   空白
+    一个以上       *    零个以上         [..] 字符集合
(..) 分组           r"..." 字符串前加 r</code></pre>

    <h2>search / findall / fullmatch</h2>
<pre><code>import re

re.search(r"\d+", "id=7 编号 2026").group()   # "7"（第一个）
re.findall(r"\d+", "id=7 编号 2026")          # ["7", "2026"]（全部）

# 校验必须整段：fullmatch（search 会漏判前后非法字符）
re.fullmatch(r"\d{11}", "13812345678")        # 匹配对象
re.fullmatch(r"\d{11}", "1381234567x")        # None（末尾多一个字母）</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <strong>校验输入要用 <code>fullmatch</code> 而不是 <code>search</code></strong>。
        <code>search</code> 只找中间一段，遇到 <code>"abc13812345678xyz"</code> 也以为合法。
        <code>fullmatch</code> 要求从头到脚完全对上。
      </p>
    </div>

    <h2>分组：取出不同段</h2>
<pre><code>m = re.search(r"([a-z]+)(\d+)", "abc123")
m.group(1)   # "abc"
m.group(2)   # "123"

# findall 有分组时返回元组列表
re.findall(r"(\d{4})-(\d{2})", "2026-08 与 1999-12")  # [("2026","08"), ("1999","12")]</code></pre>

    <h2>替换：sub</h2>
<pre><code>re.sub(r"\d+", "#", "订单 7 号共 3 件")  # "订单 # 号共 # 件"</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">raw 字符串</span>
      <p>
        模式前加 <code>r</code>，如 <code>r"\d+"</code>，反斜杠按字面解释，
        否则 <code>"\d"</code> 会被 Python 解析成转义。忘了 r 是最常见报错来源之一。
      </p>
    </div>

    <h2>配课怎么练</h2>
    <ol>
      <li>先跑 <code>32_re.py</code>，对照输出，重点看 findall 有分组时变元组的现象。</li>
      <li>再打开 <code>32_re_exercise.py</code>，6 题：抠数字、提邮箱、校验手机号、取年月日、压缩空白、校验 IP。</li>
      <li>题 3/6 是「校验」，用 <code>fullmatch</code>；题 2 邮箱可放宽到 <code>[\w.]+@[\w.]+</code>。</li>
    </ol>

    <h2>收束</h2>
    <p>
      正则别一次背太多。先背那八个，加上 search/findall/fullmatch/sub 四个函数，
      就能应付大多数「从文本里抠东西」。下一课是 <code>argparse</code>（菜单程序升级成命令行工具）。
    </p>
  </div>
</template>