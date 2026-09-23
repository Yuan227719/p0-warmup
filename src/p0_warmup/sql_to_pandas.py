
import pandas as pd


df1 = pd.DataFrame([
    {"city": "北京", "amount": "100"},
    {"city": "上海", "amount": "250"},
    {"city": "北京", "amount": "300"},
    {"city": "上海", "amount": "50"},
    {"city": "北京", "amount": "60"},
])

df2 = pd.DataFrame([
    {"user": "A", "city": "北京"},
    {"user": "A", "city": "上海"},
    {"user": "B", "city": "北京"},
    {"user": "C", "city": "上海"},
    {"user": "D", "city": "北京"},
])

df = pd.merge(df1, df2, on="city")

print(df)

df['city'] = df['city'].astype(str)
df['amount'] = df['amount'].astype(float)

df = df[df['amount'] > 100]

df_avg = df.groupby('city')[['amount']].mean()
print(df_avg)

print(df_avg.sort_values(by='amount',ascending=False).head(1))





