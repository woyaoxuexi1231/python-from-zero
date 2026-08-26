<template>
  <div class="article">
    <p>
      第 4 课会取单个：<code>names[0]</code>。
      这一课取一段（切片）、按次数循环（range）、循环时同时拿编号（enumerate）。
    </p>

    <h2>切片：取一段，不含结尾</h2>
<pre><code>names = ["小明", "hulei", "小红", "小刚"]
print(names[0:2])  # ['小明', 'hulei'] —— 没有下标 2
print(names[:2])   # 前两个
print(names[2:])   # 从 2 到尾
print(names[:])    # 整份拷贝</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>[start:end]</code> 含头不含尾。切片得到<strong>新列表</strong>，改拷贝不改原件。
        字符串切片规则相同：<code>"Python"[:3]</code> → <code>"Pyt"</code>。
      </p>
    </div>

    <h2>负数下标与步长</h2>
<pre><code>print(names[-1])    # 最后一个
print(names[-2:])   # 最后两个
print(names[:-1])   # 去掉最后一个

nums = [0, 1, 2, 3, 4, 5, 6]
print(nums[::2])    # [0, 2, 4, 6]</code></pre>

    <h2>range：需要转几圈或连续整数</h2>
<pre><code>print(list(range(3)))       # [0, 1, 2]
print(list(range(1, 4)))    # [1, 2, 3]
print(list(range(0, 6, 2))) # [0, 2, 4]

for i in range(3):
    print(f"第 {i} 圈")</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        已有列表时，直接 <code>for name in names</code>，不要先
        <code>for i in range(len(names))</code> 再下标——后者啰嗦且易错。
        range 适合：只想重复 n 次、或只要数字本身。
      </p>
    </div>

    <h2>enumerate：编号和值一起拿</h2>
<pre><code>for i, name in enumerate(names):
    print(i, name)

for rank, name in enumerate(names, start=1):
    print(f"第 {rank} 名：{name}")</code></pre>
    <p>每一轮是元组 <code>(下标, 值)</code>，用第 10 课的拆包接住。排名常用 <code>start=1</code>。</p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>切片取出中间一段、最后两个、每隔一个。</li>
      <li>用 range 打印 1~10；用 enumerate 给名单编号。</li>
      <li>对字符串切片，取出前缀/后缀。</li>
    </ol>

    <h2>收束</h2>
    <p>
      切片取段、range 计数、enumerate 带号——三个都是「遍历」的精细工具。
      下一课把 None、真假值、and/or 说清楚，避免 0 分被当成「没有」。
    </p>
  </div>
</template>
