<template>
  <div class="article">
    <p>
      列表靠编号找：<code>ages[0]</code>。很多时候你更想靠「名字」找：
      「hulei 多少分？」——这就是字典：键 → 值。
    </p>

    <h2>字典：用键找值</h2>
    <p>花括号 <code>{}</code>，写成 <code>键: 值</code>。类型标注 <code>dict[str, int]</code> 表示键是字符串、值是整数。</p>
<pre><code>scores: dict[str, int] = {
    "小明": 90,
    "hulei": 75,
    "小红": 40,
}
print(scores["hulei"])  # 75</code></pre>

    <h2>读、改、加</h2>
<pre><code>print(scores["小明"])   # 读
scores["小明"] = 95     # 改
scores["小刚"] = 60     # 原来没有的键 → 新增
print(scores)</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        键不存在直接 <code>scores["xxx"]</code> 会 <code>KeyError</code>。
        先用 <code>if "hulei" in scores:</code> 再取，或用后面课会再提的更稳妥写法。
      </p>
    </div>

    <h2>循环字典</h2>
    <p>
      <code>for name in scores</code> 拿到的是键；
      <code>for name, score in scores.items()</code> 键值一起拿（拆包，第 10 课会正式讲）。
    </p>
<pre><code>for name, score in scores.items():
    if score &gt;= 60:
        print(f"{name} 及格了，{score} 分")
    else:
        print(f"{name} 不及格，{score} 分")</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        字典的「成员判断」查的是键，不是值。
        <code>"hulei" in scores</code> 为真；<code>75 in scores</code> 一般是假（除非有人叫 75）。
      </p>
    </div>

    <h2>当函数的参数和返回值</h2>
<pre><code>def get_score(book: dict[str, int], name: str) -&gt; int:
    return book[name]

def total_score(book: dict[str, int]) -&gt; int:
    result = 0
    for score in book.values():
        result += score
    return result</code></pre>
    <p>
      <code>.values()</code> 只遍历值；<code>.keys()</code> 只遍历键；
      <code>.items()</code> 两者都要时用。
    </p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>写 <code>total_score</code>，把所有分数加起来。</li>
      <li>写 <code>passed_count</code>：统计分数 ≥ 60 的人数。</li>
      <li>故意访问不存在的键，看 <code>KeyError</code>；再用 <code>in</code> 改安全。</li>
    </ol>

    <h2>收束</h2>
    <p>
      字典解决「按名字查找」。读改加、in 防 KeyError、items 循环——这三板斧够用很久。
      下一课把变量、函数、if、列表、字典拼成一个小成绩本。
    </p>
  </div>
</template>
