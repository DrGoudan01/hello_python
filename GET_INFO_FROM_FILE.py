#__author__ = 'li'
# -*- coding:utf-8 -*-
import sys
import jisuanqi
class Config(object):
    def __init__(self,configfile):
        self.__config=[]
        with open(configfile) as file:
            for i in file :
                j = i.split('=')[1]
                self.__config.append(float(j.strip()))
    def conf(self):
        return self.__config

#员工类
class User_info(object):
    def __init__(self,infofile):
        self.__info={}
        with open(infofile) as file :
            for i in file:
                i = i.split(',')
                self.__info[i[0]]=i[1].strip()
    #定义方法，一个是文件写入，一个是对信息的修改，引入之前做的计算器部分,一个是文件输出
    def info(self):
        return self.__info
    def Calculator(self,conf,output_file):
        #在这个部分直接完成计算和写入文件
        info = self.__info
        with open(output_file) as file:
            for id in info:
                earn = int(info[id])
                if earn > conf[1]:
                    earn = conf[1]
                elif earn<= conf[1] and earn>=conf[0]:
                    pass
                else :
                    earn = conf[0]
                Shebao = earn*0.165
                Geshui = earn-Shebao
                fact_earn=jisuanqi.jisuanqi(id,earn)
                #print('{}:{}:{:.2f}:{:.2f}:{}'.format(id,info[id],Shebao,Geshui,fact_earn))
                file.write( '{},{},{:.2f},{:.2f},{}'.format(id,info[id],Shebao,Geshui,fact_earn)+'\n')







def main():
    try:
        args = sys.argv[1:]
        conf_file= args[args.index('-c')+1]
        info_file= args[args.index('-d')+1]
        output_file= args[args.index('-o')+1]
        #这部分其实可以将clss conf 合并进类中直接实现，比较方便
        main_run_conf = Config(conf_file)
        main_run = User_info(info_file)
        main_run.Calculator(main_run_conf,output_file)
    except ValueError:
        print('args  error')




if __name__ == '__main__':
    main()







