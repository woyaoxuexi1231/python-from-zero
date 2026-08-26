# ============================================================
# 第 35 课（知识讲解）：pytest —— 给函数写断言
# 运行方式：
#   1) python 35_pytest/35_pytest.py          （知识讲解）
#   2) python -m pytest 35_pytest/ -v          （看真实 pytest 绿灯）
# 安装：pip install pytest
# 配套练习：35_pytest_exercise.py
# ============================================================
import sys
from pathlib import Path

# 保证同目录 tools.py 可被 import（无论从哪启动）
_DIR = Path(__file__).resolve().parent
if str(_DIR) not in sys.path:
    sys.path.insert(0, str(_DIR))

# 痛点：改完函数靠肉眼看 print，容易漏边界；别人也没法一键验证。
# pytest（第三方）发现 test_*.py / test_* 函数，用 assert 判定对错。
# 这是 from-zero 第一课「要 pip 的」模块——不是标准库。
print("========== 第35课 pytest ==========\n")

try:
    import pytest  # noqa: F401
except ImportError:
    print("【安装】未检测到 pytest。请先执行：")
    print("  pip install pytest")
    print("  装好后再跑本课，并执行：python -m pytest 35_pytest/ -v")
    raise SystemExit(1)

print("【0】pytest 已安装。命令行查看版本：python -m pytest --version\n")


# ---------- 1. 为什么不用肉眼 print ----------
print("【1】工程习惯：可重复验证")
print("  手测：改代码 → 跑脚本 → 看输出 → 容易漏")
print("  自动测：改代码 → pytest → 绿/红，边界用例写进仓库")


# ---------- 2. 核心：assert ----------
print("\n【2】assert：条件为假就抛 AssertionError")
assert 1 + 1 == 2
assert "py" in "pytest"
print("  上面两条 assert 都过了（无输出就是好事）")
try:
    assert 1 + 1 == 3, "算术错了"
except AssertionError as e:
    print("  失败时：", e)


# ---------- 3. 命名约定：pytest 怎么找测试 ----------
print("\n【3】命名约定（自动发现）")
print("  文件：test_*.py 或 *_test.py")
print("  函数：test_ 开头")
print("  类：Test 开头（可选，类里方法仍要 test_）")
print("  本课演示：35_pytest/test_tools_demo.py")


# ---------- 4. 最小测试长什么样 ----------
print("\n【4】最小测试（对照 test_tools_demo.py）")
print("""
  # test_tools_demo.py
  from tools import add

  def test_add_positive():
      assert add(2, 3) == 5
""")


# ---------- 5. 怎么跑 ----------
print("\n【5】怎么跑")
print("  cd backend/python/from-zero")
print("  python -m pytest 35_pytest/ -v                 # 跑本课演示测试")
print("  python -m pytest 35_pytest/test_tools_demo.py::test_add_positive -v")


# ---------- 6. pytest.raises：测「会不会抛错」 ----------
print("\n【6】pytest.raises：期望抛异常")
from tools import clamp

with pytest.raises(ValueError):
    clamp(1, 10, 0)                 # lo > hi → ValueError
print("  clamp(1, 10, 0) 按预期抛 ValueError ✓")

# 还可检查异常信息：
with pytest.raises(ValueError, match="lo"):
    clamp(1, 5, 2)
print("  match= 可核对错误信息里是否含某段文字")


# ---------- 7. 参数化：一组输入共用一个测试 ----------
print("\n【7】@pytest.mark.parametrize：少写重复断言")
print("""
  @pytest.mark.parametrize("a,b,expected", [
      (1, 2, 3),
      (0, 0, 0),
      (-1, 1, 0),
  ])
  def test_add_many(a, b, expected):
      assert add(a, b) == expected
""")
print("  → 一条测试函数变成 3 个用例（demo 文件里有现成例子）")


# ---------- 8. fixture 一瞥（知道即可） ----------
print("\n【8】fixture：准备共用数据（入门知道有这东西）")
print("""
  @pytest.fixture
  def sample_name():
      return "小明"

  def test_greet(sample_name):
      assert greet(sample_name) == "你好，小明"
""")
print("  参数名对上 fixture 名，pytest 自动注入。进阶再深挖。")


# ---------- 9. 和本课练习的关系 ----------
print("\n【9】练习怎么练")
print("  ① 先跑本文件，再跑：python -m pytest 35_pytest/ -v")
print("  ② 打开 35_pytest_exercise.py，实现 6 个函数")
print("  ③ python 35_pytest/35_pytest_exercise.py 看 ✅/❌")
print("  ④ 选做：自己写 test_*.py 用 python -m pytest 再验一遍")


# ---------- 10. 易错点 ----------
print("\n【10】易错点速记")
print("  ① pytest 要 pip install，不是标准库")
print("  ② 测试函数名必须 test_ 开头，否则发现不了")
print("  ③ assert 左边实际、右边期望（习惯：assert actual == expected）")
print("  ④ 测异常用 pytest.raises，别自己 try/except 吞掉")
print("  ⑤ 在 from-zero 目录跑 pytest，保证能 import 到同目录模块")
print("  ⑥ 失败输出里有 diff：对照 Expected / Actual 改代码或改断言")


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("pip install pytest              —— 安装")
print("def test_xxx(): assert ...      —— 写测试")
print("python -m pytest path -v        —— 跑测试（推荐，不依赖 PATH）")
print("pytest.raises(Exc): ...         —— 期望抛错")
print("@pytest.mark.parametrize(...)   —— 一组数据")
print("assert 实际 == 期望             —— 判定")
