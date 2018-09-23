"""
作业1.1求亲米数
"""
# -*- coding: utf-8 -*-
#py3
 
def check(n):
    '''
    计算各因子之和模块
    '''
    s=0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            s+=i
    return s
 
if __name__ =='__main__':
    for i in range(1,300):
        res=check(i)#对1至3000所有数依次求因子和
        if i!=res and check(res)==i :#因子和不等于本身，且是亲密数，输出
            print(i,res)
#-------------------------------------------------------------------------------------------------------
for i in range(1,300):
   s=0
   for ii in range(1,int(i/2)+1):
      if(i%ii==0):
         s+=ii
   a=0
   for iii in range(1,int(s/2)+1):
      if(s%iii==0):
         a+=iii
   if(a==i and s!=i):
      print(i,"dfdfd",s)
#-------------------------------------------------------------------------------------------------------------
def fac(x):
    s=0
    for i in range(1,int(x/2)+1):
        if x%i==0:
            s+=i
    return s
num=int(input())
for i in range(1,num):
    res=fac(i)
    if i!=res and fac(res)==i and i<res :
        print("{}-{}".format(i,res))
#---------------------------------------------------------------------------------------------------------------
"""
作业1.2求默尼森系数
"""
import math
def prime(num):
    if num<=1:
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if(num%i==0):
                return False
        return True

def monisen(no):
    s=0
    for i in range(1,31):
        if(prime(i)):
            M=2**i-1
            if(prime(M)):
                s=s+1
        if(s==no):
            return M
monisen(4)
