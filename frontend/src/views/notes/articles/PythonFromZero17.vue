<template>
  <div class="article">
    <p>
      这一课<strong>不教新语法</strong>。把第 1~16 课串成一个成绩管理场景，
      每个小函数对应几课知识点——写得出来、对得上预期输出，才算真懂。
    </p>

    <h2>这一课在练什么</h2>
    <ul>
      <li>函数、默认参数、多返回值</li>
      <li>字符串、类型转换、try/except</li>
      <li>列表推导、过滤、sorted(key=)</li>
      <li>集合去重与交集</li>
      <li>切片、enumerate、None 判断</li>
      <li>class、property、对象排序</li>
    </ul>
    <p>配课文件里函数骨架已写好，把 <code>pass</code> 换成实现，跑底部自检。</p>

    <h2>怎么刷复习课</h2>
    <ol>
      <li>先读函数注释里的「要求」和「期望输出」，不要急着翻旧课文件。</li>
      <li>卡住再回到对应课号（注释里标了）。</li>
      <li>一题过一题；全绿再往下开第 18 课。</li>
    </ol>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        复习课的价值不是「再讲一遍」，而是<strong>强制检索</strong>：
        隔几天还能不能从需求还原出写法。能还原，说明进长期记忆了。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        常见翻车：0 分当「没有」、可变默认值、KeyError 不判断、
        切片含尾、sorted 忘了 reverse、class 忘了 self。
        自检失败时，对照报错类型回对应课，比盲改快。
      </p>
    </div>

    <h2>建议你自己补的几件事</h2>
    <ol>
      <li>把错题记成三行笔记：错在哪、正确写法、属于哪一课。</li>
      <li>离开答案，隔一天只凭注释再写一遍最难的两题。</li>
      <li>用自己的小数据改测试，确认不是「背输出」。</li>
    </ol>

    <h2>收束</h2>
    <p>
      第一阶段到此收束：从 print 到 class，你已经能搭交互小工具。
      下一阶段从第 18 课开始：模块拆分、生成器、pathlib——代码开始「长大」。
    </p>
  </div>
</template>
