[![CI](https://github.com/Yuan227719/p0-warmup/actions/workflows/ci.yml/badge.svg)](https://github.com/Yuan227719/p0-warmup/actions/workflows/ci.yml)

# p0-warmup

一个 CSV 数据管道工具：**读入 → 脏数据清洗 → 分组聚合 → 报告 + Parquet 落盘**，带完整的异常体系、日志和三层测试。

## 快速开始

```bash
git clone https://github.com/Yuan227719/p0-warmup.git && cd p0-warmup
uv venv && source .venv/bin/activate
uv pip install -e . pytest

p0-warmup --input orders.csv --group city --metric amount
```

输出：

```
北京 数量=4 均值=190.0
上海 数量=2 均值=150.0
杭州 数量=1 均值=999.0
深圳 数量=3 均值=125.2
```

脏数据（空值/N/A/非数字）被自动清洗，详细过程记录在日志里；结果另存为 Parquet。

## 设计决策

- **为什么双管道（手写版 + pandas 版并行）**：不是没删干净——数仓的"新旧链路双跑对账"直觉。同一份 10 万行脏数据实测：pandas 版 0.081s / 46 行，手写版 0.171s / 70 行；两版行为一致性由对拍测试永久看守。
- **为什么 to_numeric(errors="coerce") 四连清洗**：初版用 astype(float)，一列混进一个 "abc" 就整列崩；换 coerce 后又踩新坑——空格串 " " 不是 NaN，骗过 dropna 混出 15,031 行的"幽灵城市组"。最终链路：strip → 空串转 NaN → coerce → dropna，语义对照表见 pipeline_pandas.py 顶部。
- **为什么异常家族 + 退出码**：守卫最初是"记日志 + 返回空表"，实测撤退不彻底——入口拿着空表继续跑，groupby 二次爆炸。重构为 PipelineError 家族（文件缺失/空文件/列不存在），入口统一捕获 → 日志一条 → sys.exit(1)。退出码是给调度系统的：cron / DolphinScheduler 只认 0 和 1。
- **为什么 src/ 布局 + pip install -e .**：src 布局防止误 import 到未安装的工作区版本；代价是 PYTHONPATH 前缀——最终用 pyproject 的 console_scripts 根治，`p0-warmup` 裸命令诞生，前缀退役。
- **测试策略：三层金字塔 + 对拍**：单元层直调库函数断言异常家族；接口层测 main → SystemExit + 退出码；产品层跑 CLI 场景。特色是对拍测试——两套实现对同一输入必须给出相同答案，改坏任何一边当场报警。CI 曾抓到硬编码绝对路径在 Linux 上翻车——那次红勾比绿勾更有教育意义。

## 测试

```bash
pytest
```

## 数据

`orders.csv`：15 行测试数据，含 5 行脏数据（空值/非数字/N/A），用于演示清洗逻辑。`data/` 目录下有更大规模的脏数据生成器。
