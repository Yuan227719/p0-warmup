
def aggregate(rows:list[dict[str,str|float]],group_col:str,metric_col:str) -> dict[str,dict[str,float]]:
    stats = {}
    for item in rows:
        group=item[group_col]
        metric=float(item[metric_col])
        if group in stats:
            stats[group][metric_col]+=metric
            stats[group]['count']+=1
        else:
            stats[group] = {metric_col: metric, "count": 1}
    return stats

def load_rows(path:str,group_col:str,metric_col:str) -> list[dict[str,str|float]]:

    try:
        with open(path,'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：文件不存在 {path}")
        return[]

    raw_list = content.splitlines()

    if len(raw_list) < 2:
        print("错误：文件为空或只有表头")
        return[]
    
    headers = raw_list[0].split(',')
    try:
        group_index = headers.index(group_col)
        metric_index = headers.index(metric_col)
    except ValueError:
        print(f"错误：列 {group_col} 不存在，可用列：{headers}")
        return []

    load_rows = []   
    for value in raw_list[1:]:
        raw_dict= dict()


        try:
            parts = value.split(',')
            raw_dict[group_col]=parts[group_index]
            raw_dict[metric_col]=float(parts[metric_index])
        except ValueError as e:
            print('数据格式不对',e) 
            continue
        if not raw_dict[group_col].strip():
            print('跳过脏行')
            continue
        load_rows.append(raw_dict)

    return load_rows

def report(stats:dict[str,dict[str,float]],metric_col:str) -> None:
    for city,info in stats.items():
        avg = round(info[metric_col]/info['count'],1)
        print(f"{city} 数量={info['count']} 均值={avg}")

