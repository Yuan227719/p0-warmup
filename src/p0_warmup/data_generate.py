import pandas as pd
import numpy as np


def data_generate():
    n = 100_000
    df = pd.DataFrame({
        "city": np.random.choice(["北京", "上海", "深圳", "杭州", " ", "NA"], n),   # 这列本来就全是字符串，直接混着选 ✔ 没问题
        "amount": np.random.rand(n) * 1000,                                        # 先全是正常数
    })

    dirty = np.random.rand(n) < 0.1                                                # 随机圈出 ~10% 的行
    df["amount"] = df["amount"].astype(str)  
    df.loc[dirty, "amount"] = np.random.choice([" ", "abc", "NA"], dirty.sum())    # 往这些行里掺脏

    df.to_csv(r"/Users/chrisyuan/Documents/跳槽准备/python学习/p0-warmup/million_orders.csv",index=False)

if __name__ == '__main__':
    data_generate()