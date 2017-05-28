# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite o valor a ser sacado:'))
n1=n//20
n2=(n%20)//10
n3=((n%20)%10)//5
n4=(((n%20)%10)%5)//2
n5=((((n%20)%10)%5)%2)//1
print('%.d' %n1)
print('%.d' %n2)
print('%.d' %n3)
print('%.d' %n4)
print('%.d' %n5)

       