# -*- coding: utf-8 -*-
n =(input('Digite o numero de 8 algarismos: '))
x= len(n)
while x==8:
    soma=0
    while (n!== '0'):
        r=x%10
        x=(x-r)//10
        soma=soma+resto
        print (soma)
    break
while x>8 or x<8:
    print ('NAO SEI')
    break