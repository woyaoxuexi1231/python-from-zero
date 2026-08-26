<template>
  <div class="article">
    <p>
      第 4 课会用 for 往空列表里 append。
      推导式把「建空列表 → 循环 → append」压成一行。
      先会 for，再压缩；看不懂就拆回 for。
    </p>

    <h2>先写你会的 for</h2>
<pre><code>nums = [1, 2, 3, 4]
doubled = []
for n in nums:
    doubled.append(n * 2)
# [2, 4, 6, 8]</code></pre>

    <h2>同一件事，写成推导式</h2>
<pre><code>doubled = [n * 2 for n in nums]</code></pre>
    <p>读法：对可迭代里的每一项，算左边的表达式，放进新列表。</p>

    <h2>加 if：只要符合条件的</h2>
<pre><code>positives = [n for n in [-2, 0, 3, 5] if n &gt; 0]
# [3, 5]</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        句式是 <code>[表达式 for 变量 in ... if 条件]</code>。
        条件写在最后；不符合的直接跳过，不会进新列表。
      </p>
    </div>

    <h2>映射 + 过滤可以一起</h2>
<pre><code>scores = {"小明": 90, "hulei": 75, "小红": 40}
passed = [name for name, score in scores.items() if score &gt;= 60]
labels = [f"{score} 分" for score in scores.values()]</code></pre>

    <h2>什么时候别用</h2>
    <ul>
      <li>循环体步骤多、要打印、要改外部状态 → 老实写 for</li>
      <li>嵌套两层以上的推导式 → 新手先别写，可读性差</li>
    </ul>
    <p>集合、字典也有推导：<code>{...}</code> / <code>{k: v for ...}</code>。练习优先用列表 <code>[]</code>。</p>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        推导式不是越短越好。同事读不懂的一行，不如三行 for。
        Python 社区更偏向「清晰的推导式」，不是「炫技的一行」。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>把求和以外的「收集合格项」改成推导式。</li>
      <li>写「所有分数变字符串标签」的推导。</li>
      <li>同一逻辑写 for 版和推导版，对照输出。</li>
    </ol>

    <h2>收束</h2>
    <p>
      推导式是映射/过滤的短写法。下一课 lambda 与 sorted(key=)——以及 map/filter 和推导式怎么选。
    </p>
  </div>
</template>
