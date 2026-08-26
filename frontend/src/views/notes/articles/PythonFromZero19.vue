<template>
  <div class="article">
    <p>
      你一直在写 <code>for x in ...</code>。背后机制是：先 <code>iter</code> 拿迭代器，再反复
      <code>next</code>。生成器用 <code>yield</code> 写出「按需现算」的迭代器——
      数据大或要无限序列时，这是关键。
    </p>

    <h2>可迭代 vs 迭代器</h2>
    <p>列表、字符串、字典、range 都是可迭代对象。for 对它们做两件事：</p>
<pre><code>nums = [10, 20, 30]
it = iter(nums)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# 再 next → StopIteration</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        迭代器记住位置，取一个往前走一步，不能回头。
        列表可以反复 for；同一个迭代器用 <code>list(it)</code> 第二次往往是空的。
      </p>
    </div>

    <h2>自己写迭代器类</h2>
<pre><code>class Countdown:
    def __init__(self, n: int) -&gt; None:
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current &lt;= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for x in Countdown(3):
    print(x)  # 3 2 1</code></pre>

    <h2>生成器：yield 更省事</h2>
<pre><code>def countdown(n: int):
    while n &gt; 0:
        yield n
        n -= 1

for x in countdown(3):
    print(x)</code></pre>
    <p>
      函数体遇到 <code>yield</code> 就暂停交出值；下次再从断点继续。
      返回的是生成器对象，不会一次算完所有结果。
    </p>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        生成器也是一次性的。要再遍历，重新调用生成器函数。
        无限序列（如不断 yield 下一个数）不要 <code>list()</code> 收——会挂住。
      </p>
    </div>

    <h2>生成器表达式</h2>
<pre><code># 列表推导：立刻算完进内存
squares = [x * x for x in range(5)]
# 生成器表达式：惰性
squares_g = (x * x for x in range(5))</code></pre>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>用 while + next 手写复刻一次 for。</li>
      <li>写 yield 版「逐行读文件」思路（下一课会实战）。</li>
      <li>对比 list 推导与生成器表达式的内存直觉（大数据时想一想）。</li>
    </ol>

    <h2>收束</h2>
    <p>
      for = iter + next；yield 让你轻松做出惰性迭代器。
      下一课 pathlib：拼路径、扫目录、惰性读大文件。
    </p>
  </div>
</template>
