# 第 35 课演示：真实 pytest 测试（应全绿）
# 运行：python -m pytest 35_pytest/ -v
# （请在 backend/python/from-zero 目录下执行）
import pytest

from tools import add, clamp, greet


def test_add_positive():
    assert add(2, 3) == 6


def test_add_zero():
    assert add(0, 7) == 7


def test_greet_default():
    assert greet("Alice") == "你好，Alice"


def test_greet_shout():
    assert greet("Bob", shout=True) == "你好，BOB"


def test_clamp_inside():
    assert clamp(5, 0, 10) == 5


def test_clamp_below():
    assert clamp(-3, 0, 10) == 0


def test_clamp_above():
    assert clamp(99, 0, 10) == 10


def test_clamp_bad_range():
    with pytest.raises(ValueError, match="lo"):
        clamp(1, 10, 0)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
    ],
)
def test_add_many(a, b, expected):
    assert add(a, b) == expected
