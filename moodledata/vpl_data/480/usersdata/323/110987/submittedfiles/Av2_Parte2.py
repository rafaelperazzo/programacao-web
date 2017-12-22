# -*- coding: utf-8 -*-
while True:
    n=int(input('Digite um valor: '))
    if n>=1:
        break
resto1=n%10
numero1=n//10
resto2=numero1%10
numero2=n//100
resto3=numero2%10
numero3=n//1000
resto4=numero3%10
numero4=n//10000
resto5=numero4%10
numero5=n//100000
resto6=numero5%10
numero6=n//1000000
resto7=numero6%10
numero7=n//10000000
resto8=numero7%10
numero8=n//100000000
resto9=numero8%10
soma=resto1+resto2+resto3
print(soma)
    
