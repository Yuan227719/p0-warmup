# 1. 一行推导式：从 [1, 2, 3, 4, 5] 生成平方列表

rows = [1,2,3,4,5]

print([i**2 for i in rows])


# 2. 默写完整的 seen 保序去重循环，去重 [3, 1, 3, 2, 1]
rows_1=[3,1,3,2,1]

seen=set()

rows_2 = []
for x in rows_1:
    if x not in seen:
        seen.add(x)
        rows_2.append(x)


print(rows_2)

# 3. 统计 "apple banana apple cherry banana apple" 中每个单词出现次数（dict.get）
str = "apple banana apple cherry banana apple"
str_dict = dict()

for x in str.split(' '):
    str_dict[x] = str_dict.get(x,0)+1

print(str_dict)


# 4. people = [{"name": "甲", "age": 30}, {"name": "乙", "age": 25}]
#    按 age 从小到大排序（lambda 写法，生成新列表）
people = [{"name": "甲", "age": 30}, {"name": "乙", "age": 25}]
people_age = sorted(people,key=lambda x: x['age'],reverse=False)
print(people_age)


# 5. 从 "2026-09-12.csv" 中取出扩展名 "csv"
print('2026-09-12.csv'.split('.')[1])


# 6. a, (b, c) = 1, (2, 3) 执行后 a、b、c 各是什么？写成注释
'''
a=1
b=2
c=3
'''

