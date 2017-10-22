# -*- coding: utf-8 -*-
n1=int(input())
n1=str(n1)
summ=0
if len(n1)==8:
    for n in n1:
        n=int(n)
        summ=summ+n
    print(summ)
else:
    print("NAO SEI")