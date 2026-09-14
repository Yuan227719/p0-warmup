

def convert(temp):
    if temp[-1].upper() == 'C':
        try:
            value = float(temp[:-1])
        except ValueError:
            raise ValueError(f"无法解析: {temp}")
        fah = value*9/5+32
        return f"{fah:.1f}F"
    elif temp[-1].upper() == 'F':
        try:
            value = float(temp[:-1])
        except ValueError:
            raise ValueError(f"无法解析: {temp}")
        cel = (value-32)*5/9
        return f"{cel:.1f}C"
    else:
        raise ValueError(f"无法解析: {temp}")





if __name__ == "__main__":
    try:
                   # 77.0
        print(convert('25f')) # 77.00
        print(convert('abc'))   
        # print(to_fahrenheit(37))              # 98.6
        # print(to_celsius('abc'))               # 37.0
        # print(to_celsius(100, precision=0))   # 38  ← 不是 38.0，注意整数
    except ValueError as e:
        print(f'捕获异常: {e}')
