<template>
  <div class="article">
    <p>
      单个变量装一个值；现实里常常要处理「一排」：一组成绩、一串名字。
      这一课学两个搭档：<strong>列表</strong>存数据，<strong>for 循环</strong>逐项干活。
    </p>

    <h2>列表：有顺序的一排东西</h2>
    <p>方括号 <code>[]</code>，逗号分隔。类型标注 <code>list[int]</code> 表示「装满整数的列表」。</p>
<pre><code>ages: list[int] = [15, 18, 20, 12]
names: list[str] = ["小明", "hulei", "小红"]
print(names[0])    # 小明 —— 索引从 0 开始
print(len(names))  # 3</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        第一个元素是 <code>[0]</code>，不是 <code>[1]</code>。
        访问超出长度会 <code>IndexError</code>。先用 <code>len</code> 心里有数。
      </p>
    </div>

    <h2>for：把每一项拿出来做一次</h2>
<pre><code>for name in names:
    print(f"你好，{name}")</code></pre>
    <p>
      <code>name</code> 是你起的临时名字，每一轮绑定下一项。
      循环里可以再套 if——「对每一项做判断」非常常见。
    </p>
<pre><code>for age in ages:
    if age &gt;= 18:
        print(f"{age} 岁，成年")
    else:
        print(f"{age} 岁，未成年")</code></pre>

    <h2>累计：先准备盒子，再往里加</h2>
    <p>求和、计数都是同一套路：初始化 → 循环更新 → return。</p>
<pre><code>def sum_demo(numbers: list[int]) -&gt; int:
    result = 0
    for n in numbers:
        result = result + n
    return result

print(sum_demo([1, 2, 3, 4]))  # 10</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>result</code> 必须在循环外初始化。放进循环里会每圈清零；
        不初始化则第一次 <code>result + n</code> 会 <code>NameError</code>。
      </p>
    </div>

    <h2>append：往末尾加一项</h2>
<pre><code>nums: list[int] = [1, 2]
nums.append(3)
print(nums)  # [1, 2, 3]</code></pre>
    <p>
      之后做「过滤出合格的人」时，常是：空列表 + 循环 + 条件满足则 append。
    </p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>写 <code>sum_numbers</code>，对 <code>[1,2,3,4]</code> 应得到 10。</li>
      <li>写 <code>count_positive</code>：统计大于 0 的个数；<code>[-2,0,3,5]</code> → 2。</li>
      <li>先空列表，循环里把及格分数 append 进去，再 print。</li>
    </ol>

    <h2>收束</h2>
    <p>
      列表管「一排」，for 管「逐项」，累计/append 管「汇总与收集」。
      下一课字典：不靠编号，靠名字（键）找东西。
    </p>
  </div>
</template>
