# -*- coding: utf-8 -*-
from minha_bib import *
#COMECE A PARTIR DAQUI!
'''
while(True):
    while(True):
        n = int(input('Digite um número inteiro positivo: '))
        if (n >= 0):
            break
    f = 1
    for i in range (2,n+1,1):
        f *= i
    print('%d! = %d' %(n,f))
    opt = input('Deseja continuar? [S ou N]')
    if (opt == 'N'):
        print('\n\nATÉ BREVE!')
        break

n = int(input('Digite o valor de n: '))
i = 2
contador = 0
while (i < (n-1)):
    if n%i == 0 :
        contador += 1
    i += 1
if contador > 0 :
    print('%d NAO EH primo!' %n)
else:
    print('%d EH PRIMO!' %n)

i = int(input('Digite o valor de i: '))
for i in range (0,101,6):
    print(i)
   
i = int(input('Digite o valor de i: '))
for i in range (0,100,2):
    if i == 0:
        continue
    print(i)

def raiz(x,n):
    resultado = x**(1/float(n))
    return resultado
print(raiz(729,3))    

def primo(n):
    contador = 0
    for i in range (2,n,1):
        if n%i == 0:
            contador += 1
            break
    if contador == 0:
        return True
    else:
        return False
print(primo(51))

def conta_digitos(n):
    contador = 1
    while (n//10>0):
        n = n//10
        contador += 1
    return contador
print(conta_digitos(3857679))
print(conta_digitos(6597956456))

b = 0
a = 100
for i in range (0,a,1):
    if a%(i + 1) != 0:
        b = b + 1
print(b) 

print(multiplicacao(2,multiplicacao(2,4)))
'''
print(fatorial(5))