# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
print('vamos calcular a media geometrica de alguns numeros')
n = int(input('Digite a quantidade de termos:'))

a = []

for i in range (0,n,1):
    x = float(input('Digite o valor:'))
    a.append (x)
    
def mg (a):
    produto = 1
    for i in range (0,len(a),1):
        produto = produto*a[i]
    mg = produto**(1/len(a))
    return (mg)

print ('o valor da media geometrica dos seus termos é %f' %mg(a))
    