# -*- coding: utf-8 -*-
n =(input('Digite o numero de 8 algarismos: '))
x= len(n)
n = str(input('Digite o numero de 8 algarismos: '))
x= len(n)
while x==8:
    print (sum(int(i) for i in n))
    break
while x>8 or x<8:
    print ('NAO SEI')
    break