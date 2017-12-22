 -*- coding: utf-8 -*-
 
 volumei=int(input('Digite o volume inicial da televisao: '))
 trocas =int(input('Digite o numero de trocas de volume: '))
 
 for i in range (0,trocas,1):
     num=int(input('Digite a troca feita: '))
     volumei=volumei+num
     if volume>100:
         volumei=100
    elif volumei<0:
            volumei=0
print(volumei)

         