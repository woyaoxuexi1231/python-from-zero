<template>
  <div class="article">
    <p>
      到目前为止，成绩只活在内存里。程序一结束，改过的分数就没了。
      这一课三件新工具：<code>import</code>、<code>with open</code>、<code>json</code>——
      把字典写进文件，下次再读回来。
    </p>

    <h2>import：借用标准库</h2>
<pre><code>import json</code></pre>
    <p><code>json</code> 是自带的，不用 pip。文件开头写一次，后面都能用。</p>

    <h2>with open：打开文件，用完自动关</h2>
<pre><code>with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("你好，文件")

with open("demo.txt", encoding="utf-8") as f:
    text = f.read()
print(text)</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        Windows 上务必写 <code>encoding="utf-8"</code>，否则中文常乱码。
        <code>"w"</code> 会覆盖已有内容；只读可省略模式（默认 <code>"r"</code>）。
      </p>
    </div>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>with</code> 保证块结束时文件自动关闭，不必自己记 <code>close()</code>。
        第 24 课会深入「上下文管理器」；现在当「安全开关」用即可。
      </p>
    </div>

    <h2>JSON：字典 ⇄ 文本文件</h2>
<pre><code>demo = {"hulei": 75, "小明": 90}
with open("demo.json", "w", encoding="utf-8") as f:
    json.dump(demo, f, ensure_ascii=False, indent=2)

with open("demo.json", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["hulei"])</code></pre>
    <ul>
      <li><code>ensure_ascii=False</code>：中文原样写入，否则变成 <code>\uXXXX</code></li>
      <li><code>indent=2</code>：换行缩进，方便人眼打开看</li>
    </ul>

    <h2>文件不存在：try FileNotFoundError</h2>
<pre><code>def load_scores() -&gt; dict[str, int]:
    try:
        with open("scores.json", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"小明": 90, "hulei": 75, "小红": 40}

def save_scores(book: dict[str, int]) -&gt; None:
    with open("scores.json", "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)</code></pre>
    <p>启动时 <code>load</code>；改完成绩后 <code>save</code>——菜单里接到「保存」或每次修改后自动写均可。</p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>写 demo.txt / demo.json，去文件夹里用编辑器打开看一眼。</li>
      <li>实现 load / save，接到成绩本：启动读、改后写。</li>
      <li>删掉 scores.json 再跑，确认走默认成绩分支。</li>
    </ol>

    <h2>收束</h2>
    <p>
      持久化三板斧：with 开关文件、json 序列化、缺文件用 except 兜底。
      下一课换两种新容器：元组与集合。
    </p>
  </div>
</template>
