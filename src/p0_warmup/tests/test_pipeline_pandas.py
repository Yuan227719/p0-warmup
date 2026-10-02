from p0_warmup.pipeline import load_rows,aggregate,report
from p0_warmup.pipeline_pandas import load_pd,agg_pd,report_pd,PipelineError
from p0_warmup.cli import main
import pytest

def test_pandas_matches_handwritten():
    # 双跑对账：两套实现对同一输入必须给出相同答案
    rows = load_rows("orders.csv", "city", "amount")
    stats = aggregate(rows)
    df = load_pd("orders.csv", "city", "amount")
    result = agg_pd(df, "city", "amount")

    assert report(stats) == report_pd(result)

def test_cli_main(capsys):
    main(["--input", "million_orders.csv", "--group", "city", "--metric", "amount"])
    assert "上海 数量=14850 均值=501.3" in capsys.readouterr().out

    # 断言：城市集合相同；每城 count、mean(保留1位) 相同

def test_read_with_raises_file_found_fail(caplog): 
    with pytest.raises(SystemExit) as exit_value:
        print(main(["--input", "million_ers.csv", "--group", "city", "--metric", "amount"]))
    assert exit_value.value.code == 1
    assert '错误：文件不存在' in caplog.text

def test_read_with_raises_bad_columns_fail(caplog): 
    with pytest.raises(SystemExit) as exit_value:
        print(main(["--input", "million_orders.csv", "--group", "foo", "--metric", "amount"]))
    assert exit_value.value.code == 1
    assert '不存在，可用列：' in caplog.text

def test_read_with_raises_empty_file(caplog): 
    with pytest.raises(SystemExit) as exit_value:
        print(main(["--input", "orders_ony_header.csv", "--group", "city", "--metric", "amount"]))
    assert exit_value.value.code == 1
    assert '错误：文件为空或只有表头' in caplog.text

def test_load_bad_columns(): 
    with pytest.raises(PipelineError):
        load_pd("orders.csv", "foo", "amount")