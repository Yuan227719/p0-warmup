

def parse_line(line:str) -> list[str]:

    line_list = line.split(',')
    new_line=[]
    for value in line_list:
        if '\"' in value and value[0] == '\"' and value[-1] != '\"':
            tmp_value=value.strip('\"')
        elif '\"' in value and value[-1] == '\"' and value[0] != '\"':
            new_line.append(f"{tmp_value},{value.strip('\"')}")
        elif '\"' in value and value[-1] == '\"' and value[0] == '\"':
            new_line.append(value.strip('\"'))
        else:
            new_line.append(value)
    return new_line


# 写一个函数: parse_line(line: str) -> list[str]

print(parse_line("a,b,c"))          # → ['a', 'b', 'c']
print(parse_line('"a,x",b,c'))      # → ['a,x', 'b', 'c']
print(parse_line('"a,x","b,y",c'))  # → ['a,x', 'b,y', 'c']
print(parse_line(',"b",c'))         # → ['', 'b', 'c']
print(parse_line('"a,x", b ,c'))    # → ['a,x', ' b ', 'c']   (引号外的空格是否保留，自己决定并写进注释)







