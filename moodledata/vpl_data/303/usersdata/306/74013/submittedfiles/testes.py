# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input("Digite o valor a ser sacado: R$ "))

resto1=a%20
resto2=a%10
resto3=a%5
resto4=a%2
resto5=a%1

if a%20>=20:
    resto1=a%20
    qnt20=a//20
    print(qnt20)
elif resto1%10>=10:
    resto2=a%10
    qnt10=a//10
    print(qnt10)
elif resto2%5>=5:
    resto3=a%5
    qnt5=a//5
    print(qnt5)
elif resto3%2>=1:
    resto4=a%2
    qnt2=a//2
    print(qnt2)
elif resto4%1>=1:
    resto5=0
    qnt1=a//1
    print(qnt1)
    
