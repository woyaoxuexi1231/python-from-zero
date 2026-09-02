# Python 项目结构是怎么一步步变成今天这样的？

> 写给正在读 `rag-ingest` / `rag-service` 的你。  
> 这不是官方教材原文翻译，而是按「老师讲课」的方式，把 **为什么会变成现在这样** 串成一条故事线。  
> 读完你应能回答：最开始长啥样 → 中间痛在哪 → 为什么会有包、`__main__.py`、`pyproject.toml`、`uv run`。

---

## 开场：先把误会拿掉

很多人第一次看到现代 Python 项目会想：

> 「怎么又是 `__init__`，又是 `__main__`，又是 `pyproject.toml`，又是 `uv`？Java 不就一个启动类吗？」

其实 Python **和 Java 一样**：一个项目、很多模块、少数入口。  
变复杂的不是「语言故意刁难你」，而是 **问题本身变大了**：

1. 代码从 1 个文件变成 50 个文件 → 要 **组织**
2. 你要复用别人的库，别人也要复用你的 → 要 **打包 / 安装 / 依赖**
3. 同一台机器上多个项目依赖版本打架 → 要 **虚拟环境**
4. 工具太多（setuptools / poetry / pdm / hatch / uv）→ 要 **统一配置入口**

今天的架构，是这些需求 **叠了二十多年** 的结果，不是某天突然发明的。

下面按时间线讲。每一段都有三句话：**当时怎样 → 痛点是什么 → 于是多了什么**。

---

## 第一幕：石器时代——一个 `.py` 打天下（1990s 初）

### 当时怎样

Python 早期，典型用法就是：

```text
hello.py
```

```python
print("hello")
```

运行：

```bash
python hello.py
```

没有「项目结构」这种说法。文件就是程序。

### 痛点

- 代码一长，全塞一个文件，人会疯。
- 想把「读文件」「算向量」「写数据库」拆开，没有正式规矩。

### 于是多了什么

**模块（module）**：一个 `.py` 文件就是一个模块。  
用 `import` 把别人的文件当工具箱借来用。

这是第一次架构升级：

> 从「一个剧本」→「多个场景分文件写，再拼起来」。

对应到现在：`cli.py`、`pipeline.py`、`chunking.py` 各自一个模块。

---

## 第二幕：文件夹也想当模块——包（package）出现

### 当时怎样

模块多了以后，人们自然用文件夹分类：

```text
myapp/
  cli.py
  db.py
  utils.py
```

但 Python 需要回答一个问题：

> 「这个文件夹，是随便放文件的柜子，还是一个有名字的代码单元？」

### 痛点

- 同名文件到处都是（都叫 `utils.py`），import 路径会乱。
- 需要 **层级命名空间**（很像 Java 的 `com.company.app`）。

### 于是多了什么

**包（package）**：带特殊约定的文件夹。

历史上最关键的标志就是：

```text
myapp/
  __init__.py    ← 「我是一个包」的身份证
  cli.py
  db.py
```

于是你可以写：

```python
import myapp.cli
from myapp.db import connect
```

`myapp` 是包名，`cli` 是包里的模块。  
两边双下划线的 `__init__.py`，就是故意起得很显眼的「官方特殊文件」：

- 告诉解释器：这是包；
- 也可以在里面放包级说明、版本号（你们项目里的 `__version__`）。

> 这一步解决的是：**代码怎么分层、怎么用带点号的路径引用**。  
> 还没解决「怎么优雅地启动」和「怎么发给别人安装」。

---

## 第三幕：脚本 vs 模块——`if __name__ == "__main__"` 文化

### 当时怎样

同一个文件常常身兼两职：

- 被别人 `import` 当库；
- 自己直接 `python xxx.py` 当程序入口。

### 痛点

如果文件一被 import 就自动跑主流程，库就没法用了。

### 于是多了什么

几乎每个 Python 教程都会教的写法：

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

含义是：

- 被别人 import 时，`__name__` 是模块名 → **不**自动开跑；
- 直接当脚本运行时，`__name__` 变成 `"__main__"` → 才执行 `main()`。

这是「入口」思想的雏形：  
**真正逻辑放函数里，启动只是最后敲一下开关。**

你们现在的 `cli.py` 里仍有这种味道；`__main__.py` 则是把「开关」单独拆成一个特殊文件。

---

## 第四幕：官方启动姿势——`python -m` 与 `__main__.py`

### 当时怎样

人们发现：直接 `python 某路径/文件.py` 有时会把「当前目录 / 文件所在目录」搞得很乱，相对导入容易踩坑。

### 痛点

- 希望用 **模块全名** 启动（像 Java 用全限定类名启动），而不是「依赖我现在站在哪个文件夹」。
- 包本身也想被当成「可运行程序」。

### 于是多了什么

1. **`python -m 模块名`**（规范脉络可追溯到 **PEP 338** 一带）  
   用模块方式执行，而不是「随便指定一个文件路径」。

2. **包内的 `__main__.py`**  
   当你执行 `python -m app` 时，解释器约定：去跑 `app/__main__.py`。

于是出现你们现在看到的结构：

```text
app/
  __init__.py     # 我是包
  __main__.py     # 有人 -m app 时从这里进
  cli.py          # 真正的命令行主流程
```

注意：

- **不是禁止 `main.py`**；根目录 `main.py` 仍然合法、也很常见。
- `__main__.py` 是「支持 `python -m 包名`」的官方挂钩，属于 **可选但正规** 的入口写法。

> 这一步解决的是：**启动方式与包系统对齐**。  
> 还没解决「依赖安装」和「环境隔离」。

---

## 第五幕：发给别人用——打包的史前史（约 1998–2004）

代码能在自己电脑跑不够，还要：

- 安装到系统里；
- 声明依赖；
- 上传到公共索引让别人 `install`。

### 路线大致是

| 年代感 | 东西 | 它想解决什么 |
|--------|------|----------------|
| 约 1998–2000 | **distutils** 进标准库，`setup.py` 文化开始 | 怎么 build / install 自己的代码 |
| 约 2003 | **PyPI**（Python Package Index）壮大 | 中心仓库，别靠邮件传 zip |
| 约 2004 | **setuptools** 崛起 | 依赖声明、更好安装、egg 格式等 |

这一阶段的核心文物是：

```text
setup.py
```

它是 **可执行的 Python 代码**，用来描述：项目叫啥、版本多少、依赖谁、包含哪些包。

### 痛点埋下了

`setup.py` 太灵活（因为是代码），也太难标准化：

- 工具想读元数据，往往得 **先跑一段 Python**；
- 跑之前可能还缺依赖 → 鸡生蛋蛋生鸡；
- 后来每个新工具都要兼容这摊历史。

> 这一步让 Python 有了「库生态」。  
> 代价是：打包世界开始变复杂，而且会继续复杂二十年。

---

## 第六幕：依赖地狱与虚拟环境（2000s–2010s 日常）

### 痛点（几乎每个人都撞过）

项目 A 要 `requests==2.20`，项目 B 要 `requests==2.31`，  
都装进同一个系统 Python → **互相踩脚**。

### 于是多了什么

- **virtualenv**，后来标准库有了 **`venv`**：每个项目一个隔离环境。
- **`pip`** 成为主流安装器。
- **`requirements.txt`**：把依赖版本冻住，方便 `pip install -r`。

典型工作流变成：

```bash
python -m venv .venv
source .venv/bin/activate   # Windows 则是 .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

> 这一步解决的是：**项目与项目之间的依赖隔离**。  
> 结构上，业务代码仍是「包 + 模块」；多出来的是 **环境与依赖清单**。

---

## 第七幕：安装格式升级——从 egg 到 wheel

setuptools 早期有 **egg**。  
后来社区推 **wheel**（PEP 427 等）：更标准的分发格式，安装更快更可预测。

对你学项目结构的意义是：

> 「包」不只是文件夹概念，还是 **可安装、可上传 PyPI 的制品**。  
> 所以现代项目会在配置里写 `packages`、`[project.scripts]` 等——为的是安装后能出现命令行入口。

你们 `pyproject.toml` 里的：

```toml
[project.scripts]
zhien-ingest = "app.cli:main"
```

意思就是：安装之后，系统里多一个命令 `zhien-ingest`，指向 `app.cli:main`。  
这和 Java 打成 jar 再配启动脚本，是同一类需求。

---

## 第八幕：大家受不了了——`pyproject.toml` 统一战场（约 2016 起）

### 痛点总结

到 2010 年代中后期，现场常常是：

- `setup.py` / `setup.cfg` / `requirements.txt` / `Pipfile` / 各种工具私有配置 **同时存在**；
- 想换构建后端极难；
- 「先执行 setup.py 才能知道项目信息」让自动化很脆。

### 于是多了什么（关键 PEP，值得记名字）

| PEP | 大概干了啥 |
|-----|------------|
| **PEP 518** | 引入 **`pyproject.toml`**，先声明「构建这个项目需要哪些构建工具」 |
| **PEP 517** | 规定构建后端标准接口，pip 不必死绑 setuptools |
| **PEP 621** | 把项目元数据（名、版本、依赖、脚本入口等）标准化进 `pyproject.toml` 的 `[project]` |
| **PEP 660** 等 | 继续补齐可编辑安装等现代能力，让 `setup.py` 越来越「可选项」 |

于是现代项目的「户口本」变成：

```text
pyproject.toml
```

你们的 `rag-ingest` 正是这一阶段的产物：

- 依赖写在 `[project]`；
- 开发依赖可以写在 dependency groups；
- 入口脚本写在 `[project.scripts]`；
- 用 setuptools / hatchling 等作为 build-backend。

> 这一步解决的是：**用一份声明式配置，替代「必须跑 setup.py 才知道自己是谁」**。  
> 业务代码的包结构（`app/`）其实早就定型了；变的是 **外围工程文件**。

---

## 第九幕：工具大战与 `uv` 这种新玩家（近年）

有了 `pyproject.toml` 标准，工具可以百家争鸣：

- Poetry、PDM、Hatch、pip-tools……
- 以及现在很火的 **uv**（Astral）：强调速度，但仍围绕同一套现代标准转。

你们文档里的：

```powershell
uv sync
uv run python -m app --build
```

可以翻译成老师口吻：

1. `uv sync`：按锁文件 / 配置，把虚拟环境和依赖准备好（进化版的 venv + pip install）。
2. `uv run ...`：在这个环境里执行后面的命令（少一步手动 activate）。
3. `python -m app`：走包的官方启动挂钩（`__main__.py`）。

所以：**`uv` 没有发明包结构**；它是站在「包 + pyproject」这条历史线上的新扳手。

---

## 第十幕：目录摆放的两种主流——flat vs src

即使到了今天，业务代码放哪仍有两派，**都被包装指南认可**：

### Flat layout（你们现在接近这种）

```text
rag-ingest/
  pyproject.toml
  app/
    __init__.py
    __main__.py
    cli.py
  tests/
```

简单、直观，适合中小工具和服务。

### Src layout

```text
rag-ingest/
  pyproject.toml
  src/
    app/
      ...
  tests/
```

多一层 `src/`，好处是：强制你通过「安装到环境」再导入，减少「误把未安装的源码目录当正式包」的测试假象。

> 这不是对错题，是工程品味题。  
> 你们项目选 flat + `app/`，完全正常、业界常见。

---

## 把整条时间线收成一张地图

```text
单文件脚本
    ↓ 代码变长
多文件 + import（模块）
    ↓ 需要命名空间
包（文件夹 + __init__.py）
    ↓ 需要干净的启动方式
if __name__ == "__main__"
    ↓ 再对齐包系统
python -m  +  __main__.py
    ↓ 需要分享与依赖
distutils / setuptools / PyPI / setup.py
    ↓ 依赖打架
venv + pip + requirements.txt
    ↓ 分发格式与工具混乱
wheel + 多工具并存
    ↓ 需要统一声明
pyproject.toml（PEP 518/517/621…）
    ↓ 需要更好用的工作流
poetry / pdm / hatch / uv …
    ↓
你今天看到的 rag-ingest
```

每一层都不是推翻上一层，而是 **叠上去**：

- 最内核：仍然是模块与包；
- 中间：入口约定（`__main__` / scripts）；
- 外圈：环境、依赖、构建、锁文件。

---

## 对照你们正在学的项目（把抽象变具体）

以 `rag-ingest` 为例：

| 你看到的 | 它来自历史的哪一层 |
|----------|-------------------|
| `app/chunking.py` 等 | 模块拆分 |
| `app/__init__.py` | 包身份证 |
| `app/__main__.py` | `python -m app` 官方入口挂钩 |
| `app/cli.py` 的 `main()` | 「真正的启动逻辑」，像当年的 main 函数 |
| `knowledge/`、`.env` | 数据与配置外置（工程实践，不单是语言特性） |
| `pyproject.toml` | 现代项目户口本 |
| `uv.lock` | 依赖可复现（锁文件文化） |
| `uv run python -m app --build` | 新工具 × 老约定 |

`rag-service` 同理：仍是包结构；入口常表现为 `uvicorn app.main:app` 这种「模块路径:对象」，也是同一条「用导入路径定位入口」的思想。

---

## 老师小结：你该记住的不是年表，是因果

1. **最开始真的就是 `main.py` 思维**——单文件、直接跑。  
2. **包结构出现，是因为代码与协作规模变大**，需要命名空间，不是为了炫技。  
3. **`__` 显眼包文件名**，是语言拿特殊文件名当协议挂钩。  
4. **`__main__.py` 不是取代 `main.py` 的宗教**，而是「包可被 `-m` 启动」的挂钩；根目录 `main.py` 仍然合法。  
5. **`pyproject.toml` / `uv` 解决的是工程与生态问题**，不是改写 Python 语法。  
6. 你现在学的「现代架构」，本质是：

> **包组织代码 + 明确入口 + 声明式项目元数据 + 隔离环境。**

把这四句话吃透，再看任何 Python 后端/工具项目，都不会再觉得「莫名其妙一堆文件」。

---

## 建议你怎么用这篇笔记

1. 先通读一遍，建立时间感。  
2. 回到 `app/__init__.py`、`app/__main__.py`，看注释会对上号。  
3. 下一课啃 `cli.py` 时，把它理解成：**历史第三幕的 `main()`，只是搬进了包里。**

---

## 想继续深挖时可以搜的关键词（选修）

- PEP 338（`python -m`）
- Python 文档：`__main__` — Top-level code environment
- PEP 517 / 518 / 621（`pyproject.toml`）
- PyPA Packaging User Guide（包装用户指南）
- Packaging layout：`src` layout vs flat layout

---

*文档性质：学习讲义，放在代码之外，不参与运行。*
