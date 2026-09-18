# tests/test_pipeline.py
from p0_warmup.pipeline import load_rows, aggregate     # ① 把被测函数当普通模块 import

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


def test_load_rows_bad_column():     # 边界
    assert load_rows("orders.csv", "foo", "amount") == []

def test_load_rows_dirty_skipped():  # 异常/脏：15 行进、10 行出
    assert len(load_rows("orders.csv", "city", "amount")) == 10

def test_read_with_retry_raises():   # 你昨天刚立的契约
    import pytest
    from p0_warmup.read_with_retry import read_with_retry # read_with_retry 在 exercise/ 里，能 import 到就测；import 不到就挪个位置或复制函数——自己决定，注释里写理由
    with pytest.raises(FileNotFoundError):
        print(read_with_retry("nope.csv", retries=1))    # retries=1，别让 sleep 拖慢测试