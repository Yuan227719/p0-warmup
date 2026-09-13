def to_fahrenheit(celsius, precision=1):

    fah = celsius*9/5+32

    return f"{fah:.{precision}f}"




def to_celsius(fahrenheit, precision=1):

    cel = (fahrenheit-32)*5/9
    
    return f"{cel:.{precision}f}"




if __name__ == "__main__":
    print(to_fahrenheit(25))              # 77.0
    print(to_fahrenheit(25, precision=2)) # 77.00
    print(to_fahrenheit(37))              # 98.6
    print(to_celsius(98.6))               # 37.0
    print(to_celsius(100, precision=0))   # 38  ← 不是 38.0，注意整数

