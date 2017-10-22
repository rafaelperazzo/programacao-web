a = int(input('Digite o primeiro número da sequência: '))
b = int(input('Digite o segundo número da sequência: '))
c = int(input('Digite o terceiro número da sequência: '))
d = int(input('Digite o quarto número da sequência: '))

lista=[a, b, c, d]
soma = 0
h=len(lista)

if lista[0]>lista[1]:
    soma = soma +1
if lista[0]==lista[1]:
    soma = soma + 0

if lista[h-2]<lista[h-1]:
    soma= soma +1
if lista[h-2]==lista[h-1]:
    soma = soma + 0
    
for i in range(1,h-2):
    if lista[i]>lista[i-1] or lista[i]>lista[i+1]:
        soma=soma+1
    if lista[i]==lista[i-1] and lista[i]==lista[i+1]:
        soma=soma+0
    i=i+1

if soma==1:
    print('S')
if not soma==1:
    print('N')

#---------------------------------------------------------------------------------------------------------------------------------

t1=int(input('Digite o número de tomadas da régua 1: '))
t2=int(input('Digite o número de tomadas da régua 2: '))
t3=int(input('Digite o número de tomadas da régua 3: '))
t4=int(input('Digite o número de tomadas da régua 4: '))

while t1<=1:
    t1=int(input('Entrada inválida. Digite o número de tomadas da régua 1: '))
if t1>1:
    while t2<=1:
        t2=int(input('Entrada inválida. Digite o número de tomadas da régua 2: '))
    if t2>1:
        while t3<=1:
            t3=int(input('Entrada inválida. Digite o número de tomadas da régua 3: '))
        if t3>1:
            while t4<=1:
                t4=int(input('Entrada inválida. Digite o número de tomadas da régua 4: '))
            if t4>1:
                k=(t1+t2+t3+t4)-3
                print(k)

#-----------------------------------------------------------------------------------------------------------------------------------

from minha_bib import algarismos
    
num = int(input('Digite um número inteiro: '))
alg=algarismos(num)
if alg==8:
    soma=0
    for i in range(0,8,1):
        k=int(num%10)
        num=num//10
        soma=soma + k
    print(soma)
    
else:
    print('NAO SEI')

#--------------------------------------------------------------------------------------------------------------------------------
from minha_bib import fatorial

n = int(input('Digite um número inteiro não-negativo: '))
while n<0:
    print('Entrada inválida')
    n = int(input('Digite um número inteiro não-negativo: '))
if n==0:
    print('0! = 1')
if n==1:
    print('1! = 1')
if n>1:
   print('%d! = %d' % (n, fatorial(n)))