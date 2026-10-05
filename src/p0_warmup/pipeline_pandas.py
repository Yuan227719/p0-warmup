"""
pipeline_pandas —— 手写管道的 pandas 平行实现（双跑对照版）

与手写版(pipeline.py)的语义对照：
  1. 试探转换: try float/except跳过  ↔  to_numeric(errors="coerce")
  2. 清洗:     跳行有打印报告       ↔  dropna 静默清扫（透明性靠 report 补）
  3. 空值判断: strip+判空(逐行)     ↔  str.strip() + 布尔掩码过滤(整列)
     ⚠️ 实测坑：dropna 只认 NaN，" "(空格串)能存活——空城市组事故 2026-09-28
  4. 行序:     首次出现             ↔  groupby(sort=False)
  5. 计数类型: int                  ↔  agg 后 count 可能被上浮成 float，出口 astype(int)

性能（10 万行脏数据, million_orders.csv, 2026-09-28, 本机）:
  pandas 版:  0.081 s
  手写版:     0.171 s
  代码行数:   pandas 46 行 / 手写 70 行
"""

import logging

import numpy as np
import pandas as pd


class PipelineError(Exception):...        # 基类：管道类错误的总姓
class FileMissingError(PipelineError):...
class EmptyFileError(PipelineError):...
class ColumnNotFoundError(PipelineError):...


logger = logging.getLogger(__name__)

def agg_pd(df:pd.DataFrame,group_col:str,metric_col:str) -> pd.DataFrame:
    # GroupStats: dict[str, float]
    df = df.groupby(group_col,sort=False)[metric_col].agg(['sum','count','mean']).round(1)

    return df

def load_pd(path:str,group_col:str,metric_col:str) -> pd.DataFrame:

    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        # logger.warning(f"错误：文件不存在 {path}")
        raise FileMissingError(f"错误：文件不存在 {path}")
        # print(f"错误：文件不存在 {path}")
        # return pd.DataFrame()  

    if df.shape[0] < 2:
        # logger.warning(f"错误：文件为空或只有表头")
        raise EmptyFileError("错误：文件为空或只有表头")
        # print("错误：文件为空或只有表头")
        # return pd.DataFrame()  

    if group_col not in df.columns:
        # logger.warning(f"错误：列 {group_col} 不存在，可用列：{df.columns}")
        raise ColumnNotFoundError(f"错误：列 {group_col} 不存在，可用列：{list(df.columns)}")

    if metric_col not in df.columns:
        # logger.warning(f"错误：列 {metric_col} 不存在，可用列：{df.columns}")
        raise ColumnNotFoundError(f"错误：列 {metric_col} 不存在，可用列：{list(df.columns)}")    
        # return pd.DataFrame()

    original_rows = df.shape[0]

    df[metric_col] = pd.to_numeric(df[metric_col], errors="coerce")

    df[group_col] = df[group_col].str.strip()          # 剥首尾空白（向量化 strip）

    nan_ratio = df.replace("", np.nan).isna().mean()
    logger.debug(f"空值率（清洗前）：{group_col} {nan_ratio[group_col]:.1%} | {metric_col} {nan_ratio[metric_col]:.1%}")
    
    df = df[df[group_col] != ""]                        # 空串过滤（又是布尔掩码）
      
    df = df.dropna()
    final_rows = df.shape[0]
    skipped_rows = original_rows - final_rows

    logger.debug(f'原始行数：{original_rows} 清洗后行数：{final_rows} 跳过行数：{skipped_rows}')
    # print(f'原始行数：{original_rows}\n清洗后行数：{final_rows}\n跳过行数：{skipped_rows}')

    

    return df

def report_pd(df: pd.DataFrame) -> None:
    df.to_parquet("report.parquet")
    for group, row in df.iterrows():
        print(f"{group} 数量={row['count']:.0f} 均值={row['mean']:.1f}")


