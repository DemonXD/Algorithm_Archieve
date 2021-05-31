#################################
# Date: 2021/05/28
# Author: Miles Xu
# Email: kanonxmm@163.com
# Desc.: 大文件排序
#################################
# -*- coding: utf-8 -*-

###############pandas 版###############

import time
import pandas as pd
from tqdm import tqdm
i = 0
 
def reader_pandas(file, sep='\n', chunkSize=5000000, patitions=21, header=None) -> None:
    """
        Input:
            :paras file：文件名；
            :paras sep：读入时按此分隔符分割
            :paras chunkSize：切割后每个小文件的大小
            :paras patitions：进度条大小
        Output:
            None
    """
    reader = pd.read_csv(file, iterator=True)
    chunks = []
    i = 0
    with tqdm(range(patitions), 'Reading ...') as t:
        for _ in t:
            try:
                chunk = reader.get_chunk(chunkSize)
                i += 1
                chunk.to_csv('sorted' + str(i) + '.csv', index=False, header=None)
                # chunks.append(chunk)
            except StopIteration:
                break






#################yield 版####################

def read_file(fpath): 
   BLOCK_SIZE = 1024 
   with open(fpath, 'rb') as f: 
       while True: 
           block = f.read(BLOCK_SIZE) 
           if block: 
               yield block 
           else: 
               return