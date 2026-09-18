# 第 9 课：文件与 JSON

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门

**摘要**：import、with open 与 UTF-8、json.dump/load、FileNotFoundError 默认成绩、持久化成绩本。

---

到目前为止，成绩只活在内存里。程序一结束，改过的分数就没了。 这一课三件新工具：`import`、`with open`、`json`—— 把字典写进文件，下次再读回来。

## import：借用标准库

```python
import json
```

`json` 是自带的，不用 pip。文件开头写一次，后面都能用。

## with open：打开文件，用完自动关

```python
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("你好，文件")

with open("demo.txt", encoding="utf-8") as f:
    text = f.read()
print(text)
```

> **踩坑**
>
> Windows 上务必写 `encoding="utf-8"`，否则中文常乱码。 `"w"` 会覆盖已有内容；只读可省略模式（默认 `"r"`）。

> **原理**
>
> `with` 保证块结束时文件自动关闭，不必自己记 `close()`。 第 24 课会深入「上下文管理器」；现在当「安全开关」用即可。

## JSON：字典 ⇄ 文本文件

```python
demo = {"hulei": 75, "小明": 90}
with open("demo.json", "w", encoding="utf-8") as f:
    json.dump(demo, f, ensure_ascii=False, indent=2)

with open("demo.json", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded["hulei"])
```

- `ensure_ascii=False`：中文原样写入，否则变成 `\uXXXX`
- `indent=2`：换行缩进，方便人眼打开看

## 文件不存在：try FileNotFoundError

```python
def load_scores() -> dict[str, int]:
    try:
        with open("scores.json", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"小明": 90, "hulei": 75, "小红": 40}

def save_scores(book: dict[str, int]) -> None:
    with open("scores.json", "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=2)
```

启动时 `load`；改完成绩后 `save`——菜单里接到「保存」或每次修改后自动写均可。

## 建议你自己练的几件事

2. 写 demo.txt / demo.json，去文件夹里用编辑器打开看一眼。
4. 实现 load / save，接到成绩本：启动读、改后写。
6. 删掉 scores.json 再跑，确认走默认成绩分支。

## 收束

持久化三板斧：with 开关文件、json 序列化、缺文件用 except 兜底。 下一课换两种新容器：元组与集合。

---

上一课：[第 8 课：try / except](08-try - except.md)　|　下一课：[第 10 课：元组与集合](10-元组与集合.md)
