import argparse

import pandas as pd
from .pipeline import load_rows,aggregate,report

def main():

    df = pd.DataFrame()

    parser = argparse.ArgumentParser(description="CSV 分组统计工具")
    parser.add_argument("--input", required=True, help="CSV 文件路径")
    parser.add_argument("--group", default="city", help="分组列名")
    parser.add_argument("--metric", default="amount", help="统计列名")

    args = parser.parse_args()          # 解析命令行 → 得到 args 对象
    df = load_rows(args.input, args.group, args.metric)
    df = aggregate(df,args.group, args.metric)
    report(df)


if __name__ == '__main__':
    main()