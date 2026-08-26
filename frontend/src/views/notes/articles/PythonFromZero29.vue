<template>
  <div class="article">
    <p>
      第 25 课 <code>collections</code> 和 <code>itertools</code> 挤在一起，
      第 28 课已经单独复习了 collections。第 29 课<strong>只复习 itertools</strong>，
      把 <code>chain</code>、<code>islice</code>、<code>groupby</code>、排列组合、
      <code>accumulate</code> 练到能随手用——不教新语法，专门补熟练度。
    </p>

    <h2>这一课解决什么问题</h2>
    <ul>
      <li>看见「多个 list 拼一起 / 二维展平」→ 想到 <code>chain</code> / <code>chain.from_iterable</code></li>
      <li>看见「无限或很大，只取前 N 个」→ 想到 <code>islice</code></li>
      <li>看见「按某字段分组」→ 想到 <strong>先 sort</strong> 再 <code>groupby</code></li>
      <li>看见「笛卡尔积 / 排列 / 组合」→ 想到 <code>product</code> / <code>permutations</code> / <code>combinations</code></li>
      <li>看见「前缀和、滚动最高」→ 想到 <code>accumulate</code></li>
    </ul>

    <h2>chain：串起来、展平</h2>
<pre><code>import itertools

list(itertools.chain([1, 2], [3], [4, 5]))           # [1, 2, 3, 4, 5]
list(itertools.chain.from_iterable([[1, 2], [3]]))    # [1, 2, 3]</code></pre>
    <p>
      不必先 <code>a + b + c</code> 造大 list；<code>from_iterable</code> 专门压二维。
    </p>

    <h2>islice + count / cycle：无限序列只取一段</h2>
<pre><code>list(itertools.islice(itertools.count(10), 5))       # [10, 11, 12, 13, 14]
list(itertools.islice(itertools.cycle("AB"), 6))     # A,B,A,B,A,B</code></pre>
    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        别 <code>list(itertools.count())</code>——会卡死。
        无限或很大的迭代器，用 <code>islice(it, n)</code> 截取。
      </p>
    </div>

    <h2>groupby：先排序，再分组</h2>
<pre><code>records = [("Bob", "A"), ("Amy", "B"), ("Anna", "A")]
records.sort(key=lambda r: r[1])   # 必须！按班排在一起

for cls, group in itertools.groupby(records, key=lambda r: r[1]):
    names = [name for name, _ in group]
    ...</code></pre>
    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>groupby</code> 只合并<strong>相邻</strong>且 key 相同的元素——不是 SQL 的 GROUP BY。
        相同 key 不挨着会被拆成多段；要先 <code>sort(key=…)</code>。
      </p>
    </div>
    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>group</code> 是一次性迭代器，<code>list(group)</code> 之后就被消费了，不能反复用。
      </p>
    </div>

    <h2>product / permutations / combinations</h2>
    <table class="article-table">
      <thead>
        <tr>
          <th>工具</th>
          <th>含义</th>
          <th>例 ABC 取 2</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>product</code></td>
          <td>笛卡尔积，可 repeat，有序可重复</td>
          <td><code>product("AB", repeat=2)</code> → AA,AB,BA,BB</td>
        </tr>
        <tr>
          <td><code>permutations</code></td>
          <td>排列，顺序不同算不同</td>
          <td>(A,B),(A,C),(B,A)…</td>
        </tr>
        <tr>
          <td><code>combinations</code></td>
          <td>组合，顺序不算</td>
          <td>(A,B),(A,C),(B,C)</td>
        </tr>
      </tbody>
    </table>

    <h2>accumulate：前缀累积</h2>
<pre><code>list(itertools.accumulate([1, 2, 3, 4]))              # [1, 3, 6, 10] 前缀和
list(itertools.accumulate(scores, max))                 # 截至每场最高分</code></pre>

    <h2>配课怎么练</h2>
    <ol>
      <li>先跑 <code>29_itertools_review.py</code>，对照输出理解各工具。</li>
      <li>再打开 <code>29_itertools_review_exercise.py</code>，6 题全是新场景。</li>
      <li>题 3 卡壳：回来看 groupby「先 sort」；别抄第 25 课答案。</li>
      <li>全绿后，自己用 <code>product</code> 枚举两个列表的配对，用 <code>accumulate</code> 算累计销售额。</li>
    </ol>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>用 <code>chain.from_iterable</code> 展平 <code>[[1,2],[3]]</code>。</li>
      <li>用 <code>islice(count(100), 3)</code> 取 100,101,102。</li>
      <li>把学生列表按班 <code>sort + groupby</code>，对照 exercise 题 3。</li>
      <li>用 <code>combinations</code> 从 4 人里选 2 人组队。</li>
    </ol>

    <h2>收束</h2>
    <p>
      itertools 的核心是<strong>惰性迭代</strong>：不先把所有组合算进内存，按需一个个拿。
      熟练的标志是读题选对工具，写题记得 groupby 前 sort、无限序列用 islice。
      下一课可以继续 enum、 functools，或 pathlib 进阶——你哪块虚就补哪块。
    </p>
  </div>
</template>

<style scoped>
.article-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0 1.25rem;
  font-size: 0.92rem;
}

.article-table th,
.article-table td {
  border: 1px solid var(--border-subtle, rgba(0, 0, 0, 0.12));
  padding: 0.55rem 0.65rem;
  text-align: left;
}

.article-table th {
  background: var(--surface-muted, rgba(0, 0, 0, 0.04));
  font-weight: 600;
}
</style>
