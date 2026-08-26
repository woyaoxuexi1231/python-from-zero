<template>
  <div class="article">
    <p>
      前五课是零件；这一课把它们装成一台小机器——成绩本。
      不教全新语法，练的是<strong>怎么组织一个小程序</strong>：数据、函数、主流程。
    </p>

    <h2>小程序通常长这样</h2>
    <ol>
      <li>数据（这里是成绩字典）</li>
      <li>几个各干一件事的函数</li>
      <li>从输入到输出的主流程</li>
    </ol>
<pre><code>scores: dict[str, int] = {
    "小明": 90,
    "hulei": 75,
    "小红": 40,
}</code></pre>

    <h2>函数：一事一职</h2>
<pre><code>def add_score(book: dict[str, int], name: str, score: int) -&gt; None:
    book[name] = score   # 有则改，无则加

def get_score(book: dict[str, int], name: str) -&gt; int | None:
    if name in book:
        return book[name]
    return None

def letter(score: int) -&gt; str:
    if score &gt;= 90:
        return "优秀"
    elif score &gt;= 60:
        return "及格"
    return "不及格"</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        找不到人时返回 <code>None</code>（「没有」），而不是瞎返回 0——
        因为 0 分可能是真实成绩。调用方用 <code>if score is None</code> 区分「没有」和「零分」。
      </p>
    </div>

    <h2>展示与交互</h2>
<pre><code>def print_report(book: dict[str, int]) -&gt; None:
    print("----- 成绩单 -----")
    for name, score in book.items():
        print(f"{name}: {score} 分，{letter(score)}")

def lookup() -&gt; None:
    name = input("要查询谁的分数？")
    score = get_score(scores, name)
    if score is None:
        print(f"没有 {name} 这个人")
    else:
        print(f"{name} 是 {score} 分，{letter(score)}")</code></pre>

    <h2>汇总类函数</h2>
<pre><code>def average_score(book: dict[str, int]) -&gt; float:
    total = 0
    for score in book.values():
        total += score
    return total / len(book)

def passed_names(book: dict[str, int]) -&gt; list[str]:
    names: list[str] = []
    for name, score in book.items():
        if score &gt;= 60:
            names.append(name)
    return names</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        空字典时 <code>len(book)</code> 为 0，除法会 <code>ZeroDivisionError</code>。
        入门可先假设成绩本非空；正式代码要先判空再除。
      </p>
    </div>

    <h2>主流程：串起来跑一遍</h2>
<pre><code>print_report(scores)
lookup()
# add_one()：input 姓名和分数，int 后 add_score
print_report(scores)
print(average_score(scores))
print(passed_names(scores))</code></pre>
    <p>
      现在程序是「直线」：跑完就结束。下一课用 while 做成能反复进菜单的交互。
    </p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>实现 <code>average_score</code> 和 <code>passed_names</code>，对示例数据自检。</li>
      <li>给成绩本加一个人，再打印报告，确认「改的是同一个 dict」。</li>
      <li>查一个不存在的名字，确认走 <code>None</code> 分支。</li>
    </ol>

    <h2>收束</h2>
    <p>
      组织感比新语法更重要：数据一处放、函数一事一职、主流程只负责调度。
      下一课 <code>while</code> + 菜单，让程序转圈直到你选退出。
    </p>
  </div>
</template>
