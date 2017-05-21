# -*- coding: utf-8 -*-
a=int(input('a:'))
def mdc(a,b):
    if b==0:
        return a
    return mdc(b, a % b)
def mmc(a,b):
    return abs(a*b) / mdc(a,b)
print("MMC 10 e 5-->%d" % mmc(10,5))

  
    

    