# -*- coding: utf-8 -*-
#COMECE A PARTIR DAQUI!
'''
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
'''
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