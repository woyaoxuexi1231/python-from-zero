<template>
  <div class="article">
    <p>
      成绩本已经能转圈、接错、存盘。这一课换两种容器，后面几乎每天都会碰到：
      <strong>元组</strong>（有序不可改）和 <strong>集合</strong>（去重、成员判断快）。
    </p>

    <h2>三种容器对照</h2>
    <ul>
      <li>列表 <code>list</code>：有序，可改，<code>[]</code></li>
      <li>元组 <code>tuple</code>：有序，不可改，<code>()</code></li>
      <li>集合 <code>set</code>：无序，不重复，<code>{1, 2}</code> 或 <code>set()</code></li>
    </ul>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        空集合必须写 <code>set()</code>。写成 <code>{}</code> 得到的是空<strong>字典</strong>。
        集合的 <code>{}</code> 里没有冒号；字典才是 <code>键: 值</code>。
      </p>
    </div>

    <h2>元组：像列表，但不能改</h2>
<pre><code>point: tuple[int, int] = (3, 5)
print(point[0])   # 3
# point[0] = 10   # TypeError</code></pre>

    <h2>拆包：一次解开多个值</h2>
<pre><code>x, y = point
print(x, y)   # 3 5</code></pre>
    <p>
      第 5 课其实用过：<code>for name, score in scores.items()</code>——
      每一轮就是一个 <code>(键, 值)</code> 元组在拆包。
    </p>

    <h2>函数返回多个值 = 返回一个元组</h2>
<pre><code>def min_and_max(numbers: list[int]) -&gt; tuple[int, int]:
    # ... 算出 smallest, largest
    return smallest, largest

low, high = min_and_max([8, 3, 15, 1])
print(low, high)   # 1 15</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>return a, b</code> 等价于 <code>return (a, b)</code>。
        左边几个名字接住，就是拆包；也可以一个变量整包接：<code>pair = ...</code>。
      </p>
    </div>

    <h2>集合：自动去重，in 很快</h2>
<pre><code>tags: set[str] = {"python", "java", "python"}
print(tags)   # 只有两个，重复被丢掉；顺序不一定

print("python" in tags)   # True
tags.add("go")
tags.discard("java")</code></pre>
    <p>列表去重常写成 <code>list(set(xs))</code>（顺序可能变）；只要唯一性时直接用 set。</p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>写返回「最小值、最大值」的函数，调用处拆包。</li>
      <li>用 set 对名单去重，再判断某人是否在集合里。</li>
      <li>对比 <code>{}</code> 和 <code>set()</code> 的 <code>type()</code>。</li>
    </ol>

    <h2>收束</h2>
    <p>
      元组擅长「固定几个一组」和多返回值；集合擅长去重与成员判断。
      下一课：切片、range、enumerate——取一段、按次数转、循环带编号。
    </p>
  </div>
</template>
