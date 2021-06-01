#################################
# Date: 2021/05/28
# Author: Miles Xu
# Email: kanonxmm@163.com
# Desc.: 大文件排序
#################################
# -*- coding: utf-8 -*-

import os

def save_file(l, fileno):
    filepath = "testfile/resultfile/{}" .format(fileno)

    f = open(filepath, 'a')
    for i in l:
        f.write("{}".format(i))
        f.write("\n")
    f.close()
    return filepath


def nw_merge(files):
    fs = [open(file_) for file_ in files]
    # 用来记录每一路当前最小值。
    min_map = {}
    out = open("testfile/out", "a")
    for f in fs:
        read = f.readline()
        if read:
            min_map[f] = int(read.strip())

    # 将最小值取出，　并将该最小值所在的那一路做对应的更新
    while min_map:
        min_ = min(min_map.items(), key = lambda x: x[1])
        min_f, min_v = min_
        out.write("{}".format(min_v))
        out.write("\n")
        nextline = min_f.readline() 
        if nextline:
            min_map[min_f] = int(nextline.strip())
        else:
            del min_map[min_f]

def split_file(file_path, block_size):
    f = open(file_path, 'r')
    fileno = 1
    files = []
    while True:
        lines = f.readlines(block_size)
        if not lines:
            break
        lines = [int(i.strip()) for i in lines]
        lines.sort()
        files.append(save_file(lines, fileno))
        fileno += 1
    return files

if __name__ == "__main__":
    file_path = "testfile/test.txt"
    block_size = 500*1024*1024 #500M
    num_blocks = os.stat(file_path).st_size/block_size
    files = split_file(file_path, block_size)
    nw_merge(files)
