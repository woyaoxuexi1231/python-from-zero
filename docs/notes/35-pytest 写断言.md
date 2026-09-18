# 第 35 课：pytest 写断言

`Python 从零` · 更新于 2026-08-25 · 标签：Python、入门、测试

**摘要**：pip install pytest、test_ 命名、assert、raises、parametrize；给函数写可重复验证的测试。

---

改完函数靠肉眼看 `print`，边界容易漏，别人也无法一键验证。 `pytest` 是**第三方**测试库（需 `pip install pytest`）： 自动发现 `test_*.py`，用 `assert` 判定对错。 这是 from-zero 工程习惯三件套的第一件：**测试**。 命令行推荐 `python -m pytest`（不依赖 Scripts 是否在 PATH）。

## 这一课解决什么问题

- 安装与运行：`pip install pytest` → `python -m pytest path -v`
- 命名约定：文件 `test_*.py`，函数 `test_` 开头
- `assert 实际 == 期望`
- `pytest.raises`：测会不会抛错
- `@pytest.mark.parametrize`：一组输入少写重复
- fixture 一瞥（知道即可）

## 最小例子

```python
# tools.py
def add(a, b):
    return a + b

# test_tools_demo.py
from tools import add

def test_add_positive():
    assert add(2, 3) == 5
```

在 `backend` 下执行：

```bash
python -m pytest 35_pytest/ -v
```

> **原理**
>
> pytest 扫描符合命名的文件/函数，执行它们； `assert` 失败就标红并打印期望与实际的差异。 无输出的 assert 通过 = 好事。

## 测异常

```python
import pytest

def test_bad_range():
    with pytest.raises(ValueError, match="lo"):
        clamp(1, 10, 0)
```

## 参数化

```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_many(a, b, expected):
    assert add(a, b) == expected
```

> **踩坑**
>
> `pytest` **不是**标准库，没装会 `ModuleNotFoundError`。 函数名忘了 `test_` 前缀 → 静默不跑。 在错误目录执行可能导致 `import tools` 失败——请在 `backend` 目录跑。

## 配课怎么练

2. `pip install pytest`（若尚未安装）。
4. 跑 `35_pytest.py`，再跑 `python -m pytest 35_pytest/ -v` 看全绿。
6. 打开 `35_pytest_exercise.py`，实现 6 题：sub、is_even、clip、first_word、safe_div、letter_grade。
8. 选做：仿 `test_tools_demo.py` 给练习函数写 `test_*.py`。

## 收束

带走骨架：业务函数 + `test_*.py` + `assert` + `python -m pytest -v`。 下一课是 HTTP（第 36 课）：先标准库 `urllib`/`http.server`， 再对照三方 `requests`/`Flask`；基础课最后一课。 学完 pytest + HTTP，适合大复习后自己开项目。

---

上一课：[第 34 课：logging 分级日志](34-logging 分级日志.md)　|　下一课：[第 36 课：HTTP 调用与暴露（标准库 vs 三方）](36-HTTP 调用与暴露（标准库 vs 三方）.md)
