#################################
# Date: 2021/06/21
# Author: Miles Xu
# Email: kanonxmm@163.com
# Desc.: 实现中文转数字
# 十万两千：     102000
# 一百零六：     106
# 两千零一：     2001
# 十万零二点一： 100002.1
#################################
# -*- coding: utf-8 -*-

import re

# 想法1：
#   使用正则表达式进行成对拆分，然后单独转换，最后做加法

# 想法2：
#   ...

global_dic = {
    "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6,
    "七": 7, "八": 8, "九": 9, 
    "十": 10,
    "百": 100,
    "千":  1000,
    "万": 10000

}


class Solution:
    @staticmethod
    def process(samples):
        pass



if __name__ == "__main__":
    samples = [
        "十万两千": 102000,
        "一百零六": 106,
        "两千零一": 2001,
        "十万零二点一": 100002.1
    ]

    Solution.process(samples)
