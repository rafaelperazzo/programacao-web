# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input("Digite o valor a ser sacado: R$ "))

if a%20>=0:
    qnt20=a//20
    print(qnt20)
elif a%10>=0:
    qnt10=a//10
    print(qnt10)
elif a%5>=0:
    qnt5=a//5
    print(qnt5)
elif a%2>=0:
    qnt2=a//2
    print(qnt2)
elif a%1>=0:
    qnt1=a//1
    print(qnt1)
    
