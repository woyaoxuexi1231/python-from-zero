<template>
  <div class="article">
    <p>
      第 16 课会写基础类。这一课往上走：继承复用、super 构造链、方法重写、
      多态与鸭子类型，以及 <code>isinstance</code> / 常用魔术方法。
    </p>

    <h2>为什么继承</h2>
    <ul>
      <li>复用：子类自动拥有父类属性和方法</li>
      <li>分层：共有逻辑放父类，差异放子类</li>
    </ul>
<pre><code>class Animal:
    def __init__(self, name: str):
        self.name = name
    def intro(self) -&gt; str:
        return f"我是 {self.name}"

class Dog(Animal):
    pass

print(Dog("旺财").intro())</code></pre>

    <h2>super().__init__</h2>
<pre><code>class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color</code></pre>
    <p>子类有自己的 __init__ 时，通常先把父类需要的数据交给 <code>super()</code>。</p>

    <h2>方法重写</h2>
<pre><code>class Dog(Animal):
    def sound(self) -&gt; str:
        return "汪汪！"

class Cat(Animal):
    def sound(self) -&gt; str:
        return "喵～"</code></pre>
    <p>同名方法，调到子类版本。Python 里方法天生可重写。</p>

    <h2>多态 + 鸭子类型</h2>
<pre><code>def play_with(pet):
    return pet.sound()   # 不看声明类型，看有没有 sound()

class Robot:
    def sound(self) -&gt; str:
        return "哔哔"

print(play_with(Dog()), play_with(Robot()))</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        「走起来像鸭子、叫起来像鸭子，就当它是鸭子。」
        不要求必须继承同一父类——这和许多静态类型语言的习惯不同。
      </p>
    </div>

    <h2>isinstance / issubclass</h2>
<pre><code>print(isinstance(Dog(), Animal))
print(issubclass(Dog, Animal))</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        子类写了 __init__ 却忘了 super，父类属性可能根本没初始化。
        配课有知识文件 + 练习文件，先跑通讲解再做自检。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>Animal / Dog / Cat：继承、重写 sound、play_with 多态。</li>
      <li>给子类加独有属性，构造里正确 super。</li>
      <li>做一个无继承的「有 sound」的类，验证鸭子类型。</li>
    </ol>

    <h2>收束</h2>
    <p>
      继承分层，重写定差异，鸭子类型看行为不看血统。
      下一课装饰器：不改函数体，给函数「加料」。
    </p>
  </div>
</template>
