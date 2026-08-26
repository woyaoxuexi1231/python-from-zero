<template>
  <div class="article">
    <p>
      两件事：<strong>lambda</strong>（临时小函数）和<strong>把函数当参数传</strong>
      （尤其 <code>sorted(key=)</code>）。map/filter 知道即可，日常更常写推导式。
    </p>

    <h2>lambda：当场写、不取名</h2>
<pre><code>add = lambda a, b: a + b
print(add(2, 3))  # 5

double = lambda x: x * 2</code></pre>
    <p>没有名字、没有 return 关键字，只能写一个表达式。复杂逻辑请用 <code>def</code>。</p>

    <h2>sorted(key=)：按「算出来的依据」排</h2>
<pre><code>scores = {"小明": 90, "hulei": 75, "小红": 40, "阿": 100}

by_score = sorted(scores.items(), key=lambda item: item[1], reverse=True)
by_len = sorted(scores.keys(), key=lambda name: len(name))</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>key</code> 接收一个函数：对每个元素算出「排序用的值」。
        不改原数据；<code>reverse=True</code> 从大到小。
        这是 lambda 最值得学的日常组合。
      </p>
    </div>

    <h2>map / filter：函数式写法</h2>
<pre><code>nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
# 更推荐： [x * x for x in nums]

ages = [15, 18, 20, 12]
adults = list(filter(lambda a: a &gt;= 18, ages))
# 更推荐： [a for a in ages if a &gt;= 18]</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>map</code>/<code>filter</code> 返回的是惰性迭代器，要看见列表需 <code>list(...)</code>。
        Python 里优先推导式；读别人代码时能认 map/filter 即可。
      </p>
    </div>

    <h2>函数是一等公民</h2>
    <p>
      能传进 <code>sorted</code>、<code>map</code>，也能自己写「接收函数」的高阶函数。
      第 23 课装饰器会把这件事推到极致。
    </p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>按分数、按名字长度各排一次成绩 dict。</li>
      <li>同一映射分别用 map 和推导式写，确认结果相同。</li>
      <li>对对象列表（下一课）用 <code>key=lambda s: s.score</code> 排序。</li>
    </ol>

    <h2>收束</h2>
    <p>
      lambda 适合短 key；sorted(key=) 必会；map/filter 认得出、推导式写得出。
      下一课 class：把数据和行为绑在一起。
    </p>
  </div>
</template>
