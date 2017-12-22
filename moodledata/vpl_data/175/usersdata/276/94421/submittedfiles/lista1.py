# -*- coding: utf-8 -*-

n = int(input('Digite o numeros de termos da lista: '))

a = []

for i in range (0,n,1):
    valor = float(input('Digite o elemento da lista: '))
    a.append (valor)
    
soma_impar = 0
soma_par = 0

cont_impar = 0
cont_par = 0

for i in range (0,len(a),1):
    if (a[i]%2 != 0):
        soma_impar = soma_impar + a[i]
        cont_impar = cont_impar + 1    
    else:
        soma_par = soma_par + a[i]
        cont_par = cont_par + 1
        
print (soma_impar)
print (soma_par)
print (cont_impar)
print (cont_par)
print (a)