<template>
  <div class="article">
    <p>
      <code>get_score</code> 找不到人时返回 <code>None</code>。
      这一课把「怎么判断没有」和「if 到底把什么当成真」说清楚——
      否则 0 分会被误判成「没这个人」。
    </p>

    <h2>None：专门表示没有</h2>
<pre><code>missing = None
print(type(missing))  # NoneType

def get_score(book: dict[str, int], name: str) -&gt; int | None:
    if name in book:
        return book[name]
    return None</code></pre>
    <p><code>None</code> 不是 0，也不是空字符串。接近其他语言里的 null。</p>

    <h2>判断没有：用 is None</h2>
<pre><code>score = get_score(scores, "不存在")
if score is None:
    print("没有这个人")
elif score is not None:
    print(f"{score} 分")</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>is</code> 问「是不是同一个对象」；None 全局唯一，所以用 <code>is None</code>。
        <code>==</code> 问值相等，对 None 碰巧也能用，但习惯写 <code>is</code>。
      </p>
    </div>

    <h2>if 会把很多东西当成假</h2>
    <p>在 if 里相当于 False 的常见值：</p>
    <ul>
      <li><code>None</code>、<code>False</code></li>
      <li><code>0</code>、<code>0.0</code></li>
      <li><code>""</code>、<code>[]</code>、<code>{}</code>、<code>set()</code></li>
    </ul>
    <p>其他大多数为真：非空字符串、非空列表、非零数字……</p>
<pre><code>name = ""
if not name:
    print("名字是空的")</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        hulei 若是 0 分：<code>if score:</code> 会当成假，误判「没有」。
        <strong>判断有没有值 → <code>is None</code>；判断空不空 → <code>if not name</code>；
        判断分数高低 → 写 <code>&gt;= 60</code>，别靠真假值。</strong>
      </p>
    </div>

    <h2>and / or：短路</h2>
<pre><code># and：左边假就不再算右边
# or ：左边真就不再算右边
name = input("名字：").strip() or "匿名"
print(name)</code></pre>
    <p>
      <code>or</code> 常用来给默认值：左边有内容就用左边，否则用右边。
      <code>and</code> 常用来「前置条件满足才做后面」。
    </p>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        Python 的 and/or 不一定返回 True/False，而是返回<strong>决定结果的那个操作数</strong>。
        所以 <code>"" or "匿名"</code> 得到 <code>"匿名"</code>，不是 <code>True</code>。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>给成绩本某人设 0 分，分别用 <code>if score</code> 和 <code>is not None</code> 对比。</li>
      <li>用 <code>bool()</code> 打印 None、0、""、[]、"hi" 的真假。</li>
      <li>用 <code>x or default</code> 给空输入填默认名。</li>
    </ol>

    <h2>收束</h2>
    <p>
      None 表示缺席；真假值是 if 的隐式规则；and/or 会短路且返回操作数。
      下一课函数进阶：默认参数、*args、以及「默认值不要用空列表」。
    </p>
  </div>
</template>
