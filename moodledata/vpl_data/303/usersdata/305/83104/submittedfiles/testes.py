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
'''
def conta_digitos(n):
    contador = 1
    while (n//10>0):
        n = n//10
        contador += 1
    return contador
print(conta_digitos(3857679))
print(conta_digitos(659795645656945974694546659746479707608659565666545656364726424675675673535564564425545435656425742584254254254245945457726983695645674676747674766666666666666666655555555555555555555555558999097776666666666666666655555555555555554444325678986555555444355455555555565))