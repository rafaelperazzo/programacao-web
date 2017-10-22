# -*- coding: utf-8 -*-
numero = (input('Digite o numero de oito algarismos: '))
x= len(numero)
while x==8:
    print (sum(int(i) for i in numero))
    break
while x>8 or x<8:
    print ('NAO SEI')
    break