<template>
  <div class="article">
    <p>
      日志要「几点几分」、成绩要记「哪天改的」、导出文件要「YYYYMMDD」的时间戳。
      裸手拼字符串容易错、对不齐。这一课用标准库 <code>datetime</code>
      把这几件事做对：构造、格式化、解析、加减、比较。
    </p>

    <h2>这一课解决什么问题</h2>
    <ul>
      <li>拿现在 → <code>datetime.now()</code> / <code>date.today()</code></li>
      <li>时刻变字符串 → <code>strftime</code>（文件名时间戳）</li>
      <li>字符串变时刻 → <code>strptime</code>（解析输入）</li>
      <li>加几天几小时 → <code>timedelta</code></li>
      <li>日期比大小、算间隔 → 直接 <code>&lt;</code>/<code>-</code>，差值取 <code>.days</code></li>
    </ul>

    <h2>三种口味</h2>
<pre><code>from datetime import date, time, datetime, timedelta

now = datetime.now()   # 年月日 + 时分秒 + 微秒
today = date.today()   # 只要年月日

d  = date(2026, 8, 24)        # 年、月、日
t  = time(9, 30, 15)          # 时、分、秒
dt = datetime(2026, 8, 24, 9, 30, 15)</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>date()</code>/<code>datetime()</code> 参数顺序是 <strong>年、月、日</strong>。
        最容易写反成（日,月,年），结果静默变成另一天。
      </p>
    </div>

    <h2>格式化：strftime（时刻 → 字符串）</h2>
<pre><code>dt = datetime(2026, 8, 24, 9, 30, 15)
dt.strftime("%Y-%m-%d %H:%M:%S")   # "2026-08-24 09:30:15"
dt.strftime("%Y%m%d_%H%M%S")       # "20260824_093015"  ← 文件名时间戳
dt.strftime("%A")                  # "Monday"（星期全文）</code></pre>
    <p>常用格式码：<code>%Y</code>年、<code>%m</code>月、<code>%d</code>日、<code>%H</code>时、<code>%M</code>分、<code>%S</code>秒、<code>%A</code>星期。</p>

    <h2>解析：strptime（字符串 → 时刻）</h2>
<pre><code>parsed = datetime.strptime("2026-08-24 09:30:15", "%Y-%m-%d %H:%M:%S")
# parsed == datetime(2026, 8, 24, 9, 30, 15)</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        用于解析的<strong>格式必须和字符串完全对齐</strong>，对不齐抛 <code>ValueError</code>。
        解析用户输入时通常 <code>try/except</code> 包住（第 8 课），匹配 SLO 失败回退默认值。
      </p>
    </div>

    <h2>加减：timedelta</h2>
<pre><code>tomorrow = now + timedelta(days=1)
early    = now - timedelta(days=3, hours=2)
earlier  = now + timedelta(minutes=30)

span = end - start          # 得到 timedelta
span.days                   # 整天天数
span.total_seconds()        # 总秒数</code></pre>

    <h2>比较与微调</h2>
<pre><code>now &lt; later          # True，datetime 直接比大小
now.replace(hour=0, minute=0, second=0)   # 改某字段，其余不变 → 当天零点</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">不可变</span>
      <p>
        <code>datetime</code>/<code>date</code> 都是不可变的。<code>.replace(...)</code>、<code>+ timedelta</code>
        返回<strong>新对象</strong>,要重新接住变量,原对象不变。
      </p>
    </div>

    <h2>配课怎么练</h2>
    <ol>
      <li>先跑 <code>31_datetime.py</code>，对照输出。</li>
      <li>再打开 <code>31_datetime_exercise.py</code>，6 题：文件名时间戳、解析、算间隔、问候、到期日、时长格式化。</li>
      <li>题 2 要给多个格式 <code>for fmt in [...]</code> 循环试，题 3/题 6 注意算整天和除数要整除。</li>
    </ol>

    <h2>收束</h2>
    <p>
      datetime 是「时间」的操作集：构造、格式化、解析、加减、比较,配 <code>timedelta</code> 就够日常脚本。
      下一课按标准库地图.next 是 <code>re</code>(从文本里抠字段),或先做个 26~31 的小复习。
    </p>
  </div>
</template>