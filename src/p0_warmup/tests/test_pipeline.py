import pytest
# tests/test_pipeline.py
from p0_warmup.pipeline import load_rows, aggregate, report     # ① 把被测函数当普通模块 import

def test_load_rows_normal():                             # ② 函数名必须以 test_ 开头
    rows = load_rows("orders.csv", "city", "amount")     # ③ 正常调用
    assert len(rows) == 10                               # ④ assert 断言——真假即成败


def test_aggregate_beijing():        # 昨天 600.0 案的守卫
    rows = load_rows("orders.csv", "city", "amount")
    stats = aggregate(rows)
    assert stats["北京"].count == 4
    assert stats["北京"].total == 760.0

def test_load_rows_missing_file():   # 边界
    assert load_rows("nope.csv", "city", "amount") == []


def test_load_rows_bad_column_not_found(capsys):     # 边界

    result =  load_rows("orders.csv", "foo", "amount")
    assert result == []
    assert "不存在，可用列：" in capsys.readouterr().out

def test_load_rows_dirty_skipped():  # 异常/脏：15 行进、10 行出
    assert len(load_rows("orders.csv", "city", "amount")) == 10

def test_read_with_retry_raises_fail():   # 你昨天刚立的契约
    from p0_warmup.read_with_retry import read_with_retry # read_with_retry 在 exercise/ 里，能 import 到就测；import 不到就挪个位置或复制函数——自己决定，注释里写理由
    with pytest.raises(FileNotFoundError):
        print(read_with_retry("nope.csv", retries=1))    # retries=1，别让 sleep 拖慢测试

def test_read_with_retry_raises_success():   # 你昨天刚立的契约
    from p0_warmup.read_with_retry import read_with_retry 
    assert "city,amount" in read_with_retry("orders.csv", retries=1)    # retries=1，别让 sleep 拖慢测试

def test_load_rows_empty_file():
    assert load_rows("orders_ony_header.csv", "city", "amount") == []     # 只有表头的文件 → []
def test_aggregate_all_groups():
    rows = load_rows("orders.csv", "city", "amount")
    stats = aggregate(rows)
    assert stats["北京"].count == 4
    assert stats["北京"].total == 760.0
    assert stats["上海"].count == 2
    assert stats["上海"].total == 300.0
    assert stats["深圳"].count == 3
    assert stats["深圳"].total == 375.5
    assert stats["杭州"].count == 1
    assert stats["杭州"].total == 999.0
def test_report_output(capsys):
    output = '''北京 数量=4 均值=190.0
上海 数量=2 均值=150.0
杭州 数量=1 均值=999.0
深圳 数量=3 均值=125.2'''
    rows = load_rows("orders.csv", "city", "amount")
    stats = aggregate(rows)
    report(stats)
    capture = capsys.readouterr()
    assert output in capture.out

@pytest.mark.parametrize("input",[
        "跳过脏行",
        "数据格式不对 could not convert string to float: 'N/A'",
        "数据格式不对 could not convert string to float: 'abc'",
        "数据格式不对 could not convert string to float: ''",
    ])
def test_load_rows_bad_column(input,capsys):
    rows = load_rows("bad_orders.csv", "city", "amount")
    stats = aggregate(rows)
    report(stats)
    capture = capsys.readouterr()
    assert input in capture.out
        
                # report() 的打印内容——去查 pytest 的 capsys（怎么用是你的，10min 限时）