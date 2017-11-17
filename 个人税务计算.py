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
def jisuanqi(ip,earn):
    should_push=0
    earn -= earn*0.165
    if earn<=3500:
        print('{}:{}'.format(ip,earn))
    else :
        for i in the_list_r:
            if (earn-3500) >= i[0] :
                should_push = (earn-3500)*i[1]-i[2]
                earn -= should_push
                print('{}:{:.2f}'.format(ip,earn))
                break

def panduan():
    #判断点：2.是否为负数，3.是否不能转换
    #增加对多参数的遍历
    try:
        for i in sys.argv[1:]:
            ip = int(i.split(':')[0])
            earn = int(i.split(':')[1])
            if earn<0 or ip<=0:
                raise ValueError
            jisuanqi(ip,earn)
    except ValueError:
        print("Parameter Error")
        exit()


if __name__ == '__main__':
    panduan()
