import argparse
import logging
import sys
import time

from .pipeline_pandas import PipelineError, agg_pd, load_pd, report_pd

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# 文件处理器
file_handler = logging.FileHandler("debug.log")
file_handler.setLevel(logging.DEBUG)

# 格式化
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 添加处理器
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def main(args=None):

    logger.info("程序启动")


    parser = argparse.ArgumentParser(description="CSV 分组统计工具")
    parser.add_argument("--input", required=True, help="CSV 文件路径")
    parser.add_argument("--group", default="city", help="分组列名")
    parser.add_argument("--metric", default="amount", help="统计列名")

    args = parser.parse_args(args)          # 解析命令行 → 得到 args 对象
    t0=time.perf_counter() 
    try:
        # df = load_rows(args.input, args.group, args.metric)
        df1 = load_pd(args.input, args.group, args.metric)
        if df1.empty:
            return
        # df = aggregate(df)
        df1 = agg_pd(df1,args.group, args.metric)
        # report(df)
        report_pd(df1)
        logger.info(time.perf_counter()-t0)
    except PipelineError as e:
        logger.error(e)
        sys.exit(1)


if __name__ == '__main__':
    main()