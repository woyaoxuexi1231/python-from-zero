# 第 7 课：while 与菜单

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门

**摘要**：while 条件循环、while True + break、continue、菜单选项与字符串比较。

---

第 6 课成绩本是一条直线：打印 → 查一次 → 加一次 → 结束。 真正的小工具会**转圈**：做完回到菜单，直到选退出。 工具是 `while`、`break`、`continue`。

## for vs while

- `for`：事先知道转几圈（列表有几项）
- `while`：条件还成立就继续，圈数事先不一定知道

```python
count = 3
while count > 0:
    print(count)
    count = count - 1
print("到 0 了，循环结束")
```

> **踩坑**
>
> while 里忘了改条件变量，会变成死循环。 菜单场景用 `while True` + `break` 更常见，退出条件写在分支里。

## while True + break

```python
n = 1
while True:
    print(n)
    if n == 3:
        break
    n = n + 1
```

`break`：立刻离开当前循环。菜单的「退出」几乎都这么写。

## continue：跳过本圈剩余部分

```python
n = 0
while n < 5:
    n = n + 1
    if n == 3:
        continue
    print(n)   # 1 2 4 5，跳过 3
```

> **原理**
>
> `break` 离开整个循环；`continue` 只结束这一圈，马上再测条件。 两者都只影响最近一层循环。

## 菜单：while + if 拼起来

`input()` 永远是字符串，所以和 `"1"` 比，不要和整数 `1` 比。

```python
def print_menu() -> None:
    print("1. 查看成绩单")
    print("2. 查询一个人")
    print("3. 新增/修改")
    print("0. 退出")

while True:
    print_menu()
    choice = input("请选择：")
    if choice == "1":
        print_report(scores)
    elif choice == "2":
        lookup()
    elif choice == "3":
        add_one()
    elif choice == "0":
        print("再见")
        break
    else:
        print("没有这个选项")
```

> **踩坑**
>
> `choice == 1`（整数）永远对不上——用户输入是 `"1"`。 分数输入 `abc` 时 `int` 仍会崩；下一课用 try/except 接住。

## 建议你自己练的几件事

2. 把成绩本函数接到菜单选项上，确认能反复进出。
4. 加选项「平均分和及格名单」，打印后仍回到菜单。
6. 故意选不存在的选项，确认走 else 而不是崩。

## 收束

菜单的骨架就是：`while True` → 读选择 → 分支干活 → 退出就 break。 下一课专治「输入不合法直接崩」：`try / except`。

---

上一课：[第 6 课：成绩本——拼起来](06-成绩本——拼起来.md)　|　下一课：[第 8 课：try / except](08-try - except.md)
