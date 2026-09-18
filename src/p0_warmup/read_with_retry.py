import time

def read_with_retry(path,retries=1):
    read_count = 1
    
    while read_count <= retries:
        try:
            with open(path,'r') as f:
                return f.read()
        except FileNotFoundError:
            read_count+=1
            time.sleep(1)
            
    raise FileNotFoundError(f'已重试{retries}次：{path}')


# if __name__ == '__main__':
#     print(read_with_retry(r'/Users/chrisyuan/Documents/跳槽准备/python学习/p0-warmup/orders.csv'))

#     print(read_with_retry(r'/Users/chrisyuan/Documents/跳槽准备/python学习/p0-warmup/nope.csv',2))