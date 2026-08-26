<template>
  <div class="article">
    <p>
      开资源（文件、锁、连接、事务）用完必须关。忘关 = 泄漏。
      <code>with</code> 保证：进块时准备，出块时<strong>无论是否异常</strong>都清理。
    </p>

    <h2>最常用：with 文件</h2>
<pre><code>with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("第 24 课，你好！\n")
# 到这里 f 已自动关闭，不必写 f.close()</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>with X as v:</code> ≈ 进入时 <code>v = X.__enter__()</code>，
        离开时（正常结束或抛异常）都调用 <code>X.__exit__(...)</code>。
        接近 Java 的 try-with-resources。
      </p>
    </div>

    <h2>自己写：实现 __enter__ / __exit__</h2>
<pre><code>import time

class Timer:
    def __init__(self, label: str = "步骤"):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        cost = (time.perf_counter() - self.start) * 1000
        print(f"[{self.label}] {cost:.2f} ms")
        return False   # False = 不吞异常

with Timer("循环"):
    total = sum(range(500_000))</code></pre>

    <h2>__exit__ 决定吞不吞异常</h2>
<pre><code>class SuppressZeroDivision:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is ZeroDivisionError

with SuppressZeroDivision():
    n = 1 / 0   # 被吞，不往外抛</code></pre>
    <p>返回 True 吞掉；返回 False/None 照常抛出。默认多数管理器不吞。</p>

    <h2>@contextmanager：生成器写法</h2>
<pre><code>import contextlib

@contextlib.contextmanager
def opened(path: str, mode: str = "r"):
    print(f"[进入] 打开 {path}")
    f = open(path, mode, encoding="utf-8")
    try:
        yield f
    finally:
        f.close()
        print("[退出] 已关闭")</code></pre>
    <p>yield 前 = 进入；yield 后（finally）= 退出。return 提前离开 with 块，清理照样发生。</p>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        自己实现时，清理逻辑应放在 __exit__ 或 finally，不要假设块内「一定跑到最后一行」。
        异常被吞要非常谨慎——调试期宁可往外抛。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>手写 Timer，验证块内 raise 后仍打印耗时。</li>
      <li>用 @contextmanager 包一个「假装数据库事务：成功提交 / 失败回滚」。</li>
      <li>做完配课 exercise 自检，对照知识文件查漏。</li>
    </ol>

    <h2>收束</h2>
    <p>
      <code>with</code> 解决「用完必清理」。下一课进入标准库高频工具：
      <code>collections</code> 与 <code>itertools</code>——少手写分组、计数、迭代组合。
    </p>
  </div>
</template>
