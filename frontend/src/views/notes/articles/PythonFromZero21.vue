<template>
  <div class="article">
    <p>
      不教新东西。用一个小项目把第 18~20 课串起来：
      扫文件夹里所有 <code>.txt</code>，逐行统计行数与词数，再把汇总写成 JSON。
    </p>

    <h2>三课各自贡献什么</h2>
    <ul>
      <li><strong>18 模块</strong>：工具函数放 <code>course_tools.py</code>，主文件 import；注意 __name__</li>
      <li><strong>19 生成器</strong>：yield 惰性逐行读，不一次读进内存</li>
      <li><strong>20 pathlib</strong>：rglob 找文件、<code>/</code> 拼路径、写 JSON 存盘</li>
    </ul>

    <h2>典型骨架</h2>
<pre><code>from pathlib import Path
import json
from course_tools import letter_grade, word_tokens

BASE = Path(__file__).resolve().parent

def read_nonempty(path: Path):
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield line.rstrip("\n")

# 再写：统计单文件、批量 rglob、汇总 dump 到 json</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        复习课考的是「拼装」：import 对不对、生成器是不是真 yield、
        路径是否相对 __file__。自检失败时按题号回对应课。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        在错误目录运行会导致 import 失败或找不到数据目录。
        请进入 <code>21_review/</code> 再跑主文件。空行是否计入，严格按题目要求。
      </p>
    </div>

    <h2>建议你自己补的几件事</h2>
    <ol>
      <li>五题全绿后再改一份自己的样例 txt，确认逻辑泛化。</li>
      <li>把「非空行生成器」单独拿出来，用 list() 看一眼产出。</li>
      <li>打开写出的 JSON，人工核对一个文件的统计。</li>
    </ol>

    <h2>收束</h2>
    <p>
      第二阶段中段复盘完成。下一课 OOP 进阶：继承、super、多态与鸭子类型。
    </p>
  </div>
</template>
