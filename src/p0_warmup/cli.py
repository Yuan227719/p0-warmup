import argparse
import time
import numpy as np
import pandas as pd
from .pipeline import load_rows,aggregate,report
from .pipeline_pandas import load_pd,agg_pd,report_pd


def main():

    n = 100_000
    df = pd.DataFrame({
        "city": np.random.choice(["北京", "上海", "深圳", "杭州", " ", "NA"], n),   # 这列本来就全是字符串，直接混着选 ✔ 没问题
        "amount": np.random.rand(n) * 1000,                                        # 先全是正常数
    })

    dirty = np.random.rand(n) < 0.1                                                # 随机圈出 ~10% 的行
    df["amount"] = df["amount"].astype(str)  
    df.loc[dirty, "amount"] = np.random.choice([" ", "abc", "NA"], dirty.sum())    # 往这些行里掺脏

    df.to_csv(r"/Users/chrisyuan/Documents/跳槽准备/python学习/p0-warmup/million_orders.csv")

    parser = argparse.ArgumentParser(description="CSV 分组统计工具")
    parser.add_argument("--input", required=True, help="CSV 文件路径")
    parser.add_argument("--group", default="city", help="分组列名")
    parser.add_argument("--metric", default="amount", help="统计列名")

    args = parser.parse_args()          # 解析命令行 → 得到 args 对象
    t0=time.perf_counter(); 
    df = load_rows(args.input, args.group, args.metric)
    # df1 = load_pd(args.input, args.group, args.metric)
    df = aggregate(df)
    # df1 = agg_pd(df1,args.group, args.metric)
    report(df)
    # report_pd(df1)
    print(time.perf_counter()-t0)


if __name__ == '__main__':
    main()