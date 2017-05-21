# -*- coding: utf-8 -*-
v=int(input('digite o valor que deseja sacar'))
n1=v//20
n2=(v%20)//10
n3=((v%20)%10)//5
n4=(((v%20)%10)%5)//2
n5=((((v%20)%10)%5)%2)//1

print('valor de 20 reais:%d'%n1)
print('valor de 10 reais:%d'%n2)
print('valor de 5 reais:%d'%n3)
print('valor de 2 reais:%d'%n4)
print('valor de 1 real:%d'%n5)
