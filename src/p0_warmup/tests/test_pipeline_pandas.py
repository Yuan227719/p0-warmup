from p0_warmup.pipeline import load_rows,aggregate,report
from p0_warmup.pipeline_pandas import load_pd,agg_pd,report_pd

def test_pandas_matches_handwritten():
    # 双跑对账：两套实现对同一输入必须给出相同答案
    rows = load_rows("orders.csv", "city", "amount")
    stats = aggregate(rows)
    df = load_pd("orders.csv", "city", "amount")
    result = agg_pd(df, "city", "amount")

    assert report(stats) == report_pd(result)


    # 断言：城市集合相同；每城 count、mean(保留1位) 相同