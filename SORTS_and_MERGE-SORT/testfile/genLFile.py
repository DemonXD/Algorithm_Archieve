#################################
# Date: 2021/05/28
# Author: Miles Xu
# Email: kanonxmm@163.com
# Desc.: 生成随机行大文件
#       'A' 占一个字节， 1024个 占1KB
#       ',' 占一个字节， 1024个 占1KB
#       '\n' 占两个字节， 1024个 占2KB
#################################
# -*- coding: utf-8 -*-

import random
from tqdm import trange
from typing import List

# G M KB Byte
FILE_SIZE = 20 * 1024 * 1024 * 1024 * 1 # 21474836480
# 一行安排32个字节，1KB正好可以安排32行, \n占用2个字节，可用字节为30
LINE_SIZE = 32


def randChoice(pos: int, num: int) -> List[int, str]:
    """[summary]
        返回指定串
    """
    pool_1 = ['a', 'B', 'A', 'C', 'D', '!', '?', ' ', '%', '#', '(']
    pool_2 = []
    pos_map = {
        0: pool_1,
        1: pool_2
    }
    select_pool = pos_map.get(pos, None)
    if select_pool is not None:
        return random.choices(select_pool, k=num)


def genfile():
    with open("test.txt", "w+") as f:
        for _ in trange(0, FILE_SIZE, LINE_SIZE):
            M1_SIZE = 12
            SER_NUM = random.randint(1, 700000000)
            AVAILABLE_LEN = 32 - 2 - 2 - len(str(SER_NUM))
            b1 = randChoice(0, M1_SIZE)
            LEFT_LEN = AVAILABLE_LEN - M1_SIZE
            a1 = randChoice(1, LEFT_LEN)
            f.write(f"{b1},{SER_NUM},{a1}\n")


if __name__ == "__main__":
    genfile()