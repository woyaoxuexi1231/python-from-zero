<template>
  <div class="article">
    <p>
      第 1 课会写函数，第 10 课会 <code>return a, b</code>。
      这一课让调用更省事：常不变的参数给默认值；个数不固定时用 <code>*args</code>。
    </p>

    <h2>默认参数：可以不传</h2>
<pre><code>def greet(name: str, suffix: str = "同学") -&gt; str:
    return f"{name}{suffix}"

print(greet("小明"))           # 小明同学
print(greet("小明", "老师"))   # 小明老师</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>有默认值的参数必须放在没有默认值的后面，否则 SyntaxError。</p>
    </div>

    <h2>关键字参数：按名字传</h2>
<pre><code>def letter(score: int, excellent: int = 90, passed: int = 60) -&gt; str:
    if score &gt;= excellent:
        return "优秀"
    elif score &gt;= passed:
        return "及格"
    return "不及格"

print(letter(85, passed=80))  # 及格线改成 80</code></pre>
    <p>位置参数要写在关键字参数前面。</p>

    <h2>*args：个数不固定</h2>
<pre><code>def add_all(*nums: int) -&gt; int:
    result = 0
    for n in nums:
        result += n
    return result

print(add_all(1, 2))
print(add_all(1, 2, 3, 4))
print(add_all(*[10, 20, 30]))  # 列表拆开传入</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        形参前加 <code>*</code>，函数里收到的是元组。
        调用处对列表加 <code>*</code> 是「拆包传入」，和定义处的 <code>*</code> 是一对搭档。
      </p>
    </div>

    <h2>默认值不要用空列表 / 空字典</h2>
<pre><code># 错误：def add_note(text, box=[]):  —— 多次调用会共用同一个列表
def add_note(text: str, box: list[str] | None = None) -&gt; list[str]:
    if box is None:
        box = []
    box.append(text)
    return box</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        默认值在<strong>定义函数时算一次</strong>，不是每次调用新建。
        可变对象作默认值会串数据。正确做法：默认 <code>None</code>，函数里再新建。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>写 <code>pad(text, n=3)</code>：后面补 n 个句号。</li>
      <li>写 <code>longest(*words)</code>：返回最长的那个字符串。</li>
      <li>故意用 <code>box=[]</code> 作默认值，连续调用两次，观察串数据。</li>
    </ol>

    <h2>收束</h2>
    <p>
      默认参数减负担，关键字参数提可读，*args 吃不定长；可变默认值是经典坑。
      下一课列表推导式：把「空列表 + for + append」压成一行。
    </p>
  </div>
</template>
