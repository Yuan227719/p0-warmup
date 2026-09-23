import pandas as pd


df = pd.DataFrame([
    {"city": "北京", "amount": 100},
    {"city": "上海", "amount": 250},
    {"city": "北京", "amount": 300},
    {"city": "上海", "amount": 50},
    {"city": "北京", "amount": 60},
])


df_avg = df.groupby('city').agg(count=('amount','count'),mean=('amount','mean')).round(1)

print(df_avg)