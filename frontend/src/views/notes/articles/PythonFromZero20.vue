<template>
  <div class="article">
    <p>
      第 9 课会 open / json 读写单个文件。这一课解决三个新问题：
      跨平台拼路径、遍历目录批量处理、大文件别一口气读进内存。
    </p>

    <h2>pathlib.Path：路径是对象</h2>
<pre><code>from pathlib import Path

BASE = Path(__file__).resolve().parent
demo = BASE / "demo_data"
p = BASE / "20_files_paths.py"
print(p.name, p.stem, p.suffix, p.parent)</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        用 <code>/</code> 拼接，自动处理系统分隔符。别再字符串硬拼
        <code>"a" + "/" + "b"</code>。Python 3.6+ 推荐 pathlib。
      </p>
    </div>

    <h2>建目录、写文件、列一层</h2>
<pre><code>demo.mkdir(exist_ok=True)
(demo / "note.tmp.txt").write_text("小明 90\n", encoding="utf-8")

for f in demo.iterdir():
    print(f.name)</code></pre>

    <h2>glob / rglob</h2>
<pre><code>for f in demo.glob("*.txt"):
    print(f.name)          # 当前层匹配

for f in demo.rglob("*.txt"):
    print(f)               # 递归进子目录</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>iterdir</code>/<code>glob</code> 只看一层；要钻子目录用 <code>rglob</code>。
        跑课文件时注意工作目录；用 <code>Path(__file__).parent</code> 定位最稳。
      </p>
    </div>

    <h2>大文件：逐行读（可配生成器）</h2>
<pre><code>def read_lines(path: Path):
    with path.open(encoding="utf-8") as f:
        for line in f:
            yield line.rstrip("\n")

for line in read_lines(demo / "note.tmp.txt"):
    print(line)</code></pre>
    <p>不要对巨型日志 <code>f.read()</code> 一次灌进内存；for line in f 本身就是惰性的。</p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>用 Path 拼出「本课目录 / 子目录 / 文件」并 exists 检查。</li>
      <li>glob 出所有 .txt，统计每个文件行数。</li>
      <li>把汇总结果 json.dump 到本课目录。</li>
    </ol>

    <h2>收束</h2>
    <p>
      Path 管路径，glob/rglob 管发现文件，逐行/yield 管读大文件。
      下一课复习：把 18~20 串成「扫目录 → 统计 → 写 JSON」。
    </p>
  </div>
</template>
