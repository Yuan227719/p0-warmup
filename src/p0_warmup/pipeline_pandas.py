from dataclasses import dataclass
import pandas as pd


def aggregate(df:pd.DataFrame,group_col:str,metric_col:str) -> pd.DataFrame:
    # GroupStats: dict[str, float]
    try:
        df = df.groupby(group_col,sort=False)[metric_col].agg(['sum','count','mean']).round(1)
    except ValueError:
        print(f"错误：列 {group_col} 不存在，可用列：{df.columns}")
        return pd.DataFrame()  

    return df

def load_rows(path:str,group_col:str,metric_col:str) -> pd.DataFrame:

    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"错误：文件不存在 {path}")
        return pd.DataFrame()  

    if df.shape[0] < 2:
        print("错误：文件为空或只有表头")
        return pd.DataFrame()  


    df[metric_col] = pd.to_numeric(df[metric_col], errors="coerce")

    df = df.dropna()

    return df

def report(df: pd.DataFrame) -> None:
    for group, row in df.iterrows():
        print(f"{group} 数量={row['count']:.0f} 均值={row['mean']:.1f}")


