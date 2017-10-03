# -*- coding: utf-8 -*-
num=int(input("Digite um número com 8 algarismos: "))
if 10000000<=num<100000000:
    num=str(num)
    somat=0
    for i in num:
        i=int(i)
        somat=i+somat
    print(somat)
else:
    print("NAO SEI")