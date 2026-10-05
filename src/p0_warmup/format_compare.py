import os
import time

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "city": np.random.choice(["北京","上海","深圳","杭州"], 100_000),
    "amount": np.random.rand(100_000) * 1000,
})
df.to_csv("demo.csv")
df.to_parquet("demo.parquet")

# 数字一：文件大小（os.path.getsize 或 ls -lh）
csv_size = os.path.getsize('demo.csv')
print(csv_size)
parquet_size = os.path.getsize('demo.parquet')
print(parquet_size)
# 数字二：读取耗时（time 计时，read_csv vs read_parquet 各跑一遍）
t0=time.perf_counter() 
pd.read_csv("demo.csv") 
print(time.perf_counter()-t0)
t1=time.perf_counter() 
pd.read_parquet('demo.parquet')
print(time.perf_counter()-t1)



