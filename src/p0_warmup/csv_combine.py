from re import T
import os
from numpy import empty
import pandas as pd
import glob
import logging


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 文件处理器
file_handler = logging.FileHandler("data_debug.log")
file_handler.setLevel(logging.DEBUG)

# 格式化
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 添加处理器
logger.addHandler(file_handler)

def combine_operator(path:str,headers:list):
 
    all_files = glob.glob(os.path.join(path,"*.csv"))
    final_files = glob.glob(os.path.join(path,"*.csv"))
    index = 1
    total_count = 0
    for file in all_files:
        df = pd.read_csv(file)
        columns = df.shape[0]
        if(columns<2):
            logger.warning(f"错误：文件为空或只有表头:{file}")
            final_files.remove(file)
            continue
        elif (list(df.columns) != headers):
            logger.warning(f"错误：当前文件表头不一致:{file}")
            final_files.remove(file)
            continue
        logger.info(f"第{index}个文件：{file}, 行数：{columns}")
        index = index + 1
        total_count += columns
        

    combined_csv = pd.concat((pd.read_csv(file) for file in final_files),ignore_index=True)

    logger.info(f"合并后文件行数：{combined_csv.shape[0]}")

    if total_count == combined_csv.shape[0]:
        logger.info(f"行数相等")

    combined_csv.to_csv(r'/Users/chrisyuan/Documents/跳槽准备/python学习/p0-warmup/combined_data/combined_data.csv',index=False)

if __name__ == '__main__':
    combine_operator(f"/Users/chrisyuan/Documents/跳槽准备/python学习/p0-warmup/data/",["city","amount"])