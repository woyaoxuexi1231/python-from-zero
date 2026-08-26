<template>
  <div class="article">
    <p>
      前面常用 dict 装数据，操作数据的函数另写。
      <strong>类</strong>把数据（属性）和行为（方法）绑在一起——对象带着自己的能力走。
    </p>

    <h2>第一个类</h2>
<pre><code>class Student:
    def __init__(self, name: str, score: int) -&gt; None:
        self.name = name
        self.score = score

    def is_pass(self) -&gt; bool:
        return self.score &gt;= 60

    def __str__(self) -&gt; str:
        return f"{self.name}: {self.score} 分"

s1 = Student("小明", 90)   # 不用 new
print(s1.name, s1.is_pass())
print(s1)</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>__init__</code> 是构造器，创建时自动调用。
        <code>self</code> 是「这个对象自己」（类似 this）。
        方法第一个参数必须是 self；调用时 <code>s1.is_pass()</code> 不用手动传。
      </p>
    </div>

    <h2>和 dict 对比</h2>
    <p>
      dict 版要另写 <code>is_pass(d)</code>；class 版 <code>s.is_pass()</code> 顺着对象就能调。
      行为跟着数据走，这就是 class 的价值。
    </p>

    <h2>@property：算出来的属性</h2>
<pre><code>class StudentV2:
    def __init__(self, name: str, score: int) -&gt; None:
        self.name = name
        self.score = score

    @property
    def level(self) -&gt; str:
        if self.score &gt;= 90:
            return "优秀"
        if self.score &gt;= 60:
            return "及格"
        return "不及格"

print(StudentV2("阿", 95).level)  # 像属性，不加括号</code></pre>

    <h2>对象也能排序</h2>
<pre><code>students = [Student("小明", 90), Student("hulei", 75), Student("小红", 40)]
by_score = sorted(students, key=lambda s: s.score, reverse=True)</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        列表里 print 对象要用 <code>__repr__</code>（或让它复用 <code>__str__</code>），
        否则看到的是内存地址。<code>print(s)</code> 走 <code>__str__</code>；容器调试常走 repr。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>写 Student，实现 is_pass 与 __str__。</li>
      <li>加 @property 显示等级。</li>
      <li>一组学生按分数排序后打印。</li>
    </ol>

    <h2>收束</h2>
    <p>
      class = 属性 + 方法；self 指向实例；property 把计算伪装成属性。
      下一课是复习通关：把 1~16 课串进一个成绩场景。
    </p>
  </div>
</template>
