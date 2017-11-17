#!/usr/bin/python3
#__author__ = 'li'
# -*- coding:utf-8 -*-
import sys
the_list = (
    (0,0.03,0),
    (1500,0.1,105),
    (4500,0.2,555),
    (9000,0.25,1005),
    (35000,0.3,2755),
    (55000,0.35,5505),
    (80000,0.45,13505)
)
the_list_r = the_list[::-1]
#分为计算器部分和判定参数部分
def jisuanqi(earn):
    should_push=0
    if earn<=3500:
        return '0'
    else :
        for i in the_list_r:
            if earn >= i[0] :
                should_push = (earn-3500)*i[1]-i[2]
                return '{:.2f}'.format(should_push)

def panduan():
    #判断点：1.参数是否过多，2.是否为负数，3.是否不能转换
    if len(sys.argv)>2:
        print("Parameter Error")
        exit()

    try:
        i = int(sys.argv[1])
        if i<0:
            raise ValueError
        return i
    except ValueError:
        print("Parameter Error")
        exit()


if __name__ == '__main__':
    print(jisuanqi(panduan()))
