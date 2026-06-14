# Box Planning

[中文](#中文说明) | [English](#english)

## English

A small Python optimization experiment for choosing a combination of storage boxes that best fits a target space.

The project started from a practical home-organization problem: given a cabinet / shelf size and a list of candidate storage-box sizes, find a combination that uses the space efficiently.

Related write-up: [知乎文章](https://zhuanlan.zhihu.com/p/565578114)

## Problem

Given:

- a target 3D space size, such as a shelf or cabinet;
- a table of candidate box sizes;
- a maximum number of boxes to combine;
- a cost function that penalizes unused space.

Find:

- the box combination with the lowest cost;
- several candidate combinations for comparison.

## Repository structure

```text
.
├── main.py                   # Example entry point
├── find_solver.py            # Brute-force combination solver and cost functions
├── candidate_size_1.txt      # Candidate box-size table
├── LICENSE
└── README.md
```

## How it works

The solver enumerates combinations with replacement, computes the occupied size of each combination, filters invalid combinations, and ranks candidates by a handcrafted cost function.

## Run

```bash
python3 main.py
```

You can modify these values in `main.py`:

```python
target_size = np.array([44, 43, 28])
find_solver(target_size, size_table, cost_type.height_one, 3)
```

## Keywords

`box planning`, `storage optimization`, `combination search`, `brute force search`, `Python`, `home organization`, `algorithm experiment`

---

## 中文说明

这是一个源于真实生活问题的 Python 小实验：**如何选择一组收纳盒，让它们尽可能合适地放进目标空间里**。

比如给定一个柜子 / 抽屉 / 置物架的尺寸，以及若干候选收纳盒尺寸，程序会枚举可能的组合，并根据剩余空间和手写 cost function 给出较优方案。

相关文章：[知乎：收纳盒组合规划问题](https://zhuanlan.zhihu.com/p/565578114)

## 问题定义

输入：

- 目标空间尺寸；
- 候选收纳盒尺寸表；
- 最多允许使用的盒子数量；
- 对空间浪费的惩罚函数。

输出：

- cost 最低的组合；
- 若干候选组合，便于人工比较。

## 运行方式

```bash
python3 main.py
```

可以在 `main.py` 中修改目标尺寸和搜索参数。

## 关键词

收纳盒规划、组合优化、暴力搜索、Python、生活算法、空间利用率、家居收纳。
