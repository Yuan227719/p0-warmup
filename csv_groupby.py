def aggregate(rows):
    stats = {}
    for item in rows:
        city=item['city']
        amount=float(item['amount'])
        if city in stats:
            stats[city]['amount']+=amount
            stats[city]['count']+=1
        else:
            stats[city] = {"amount": amount, "count": 1}
    return stats

def load_rows():
    with open(r'/Users/chrisyuan/Documents/跳槽准备/python学习/p0-warmup/orders.csv','r') as f:
        load_rows=[]
        content = f.read()
        raw_list = content.splitlines()
        city = str(raw_list[0].split(',')[0])
        amount = raw_list[0].split(',')[1]
    for value in raw_list[1:]:
        raw_dict = dict()
        try:
            raw_dict[city]=value.split(',')[0]
            raw_dict[amount]=float(value.split(',')[1])
        except ValueError as e:
            print('数据格式不对',e) 
            continue
        if not raw_dict[city].strip():
            print('跳过脏行')
            continue
        load_rows.append(raw_dict)
    print(load_rows)
    return load_rows

def report(stats):
    for city,info in stats.items():
        avg = round(info['amount']/info['count'],1)
        print(f"{city} 数量={info['count']} 均值={avg}")

if __name__ == "__main__":
    rows = load_rows()
    stats = aggregate(rows)
    report(stats)
