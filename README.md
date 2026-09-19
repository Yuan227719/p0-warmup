# p0-warmup
一句话：CSV 分组统计工具（读入→脏数据清洗→分组聚合→报告），带完整测试。

## 安装
git clone ... && cd p0-warmup
uv venv && source .venv/bin/activate
uv pip install pytest

## 用法
PYTHONPATH=src python -m p0_warmup.cli --input orders.csv --group city --metric amount
输出：
跳过脏行
数据格式不对 could not convert string to float: 'N/A'
数据格式不对 could not convert string to float: 'abc'
数据格式不对 could not convert string to float: ''
数据格式不对 could not convert string to float: ''
北京 数量=4 均值=190.0
上海 数量=2 均值=150.0
杭州 数量=1 均值=999.0
深圳 数量=3 均值=125.2

## 测试
PYTHONPATH=src pytest --cov=p0_warmup --cov-report=term-missing 

## 数据
orders.csv：15 行测试数据，含 5 行脏数据（空值/非数字/N/A），用于演示清洗逻辑