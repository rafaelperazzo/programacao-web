from minha_bib import *




'''
lista1 = [1,2,3,123]
a = lista1[len(lista1)-1]
print(a)
'''

'''
n = int(input('Digite a quantidade de elementos: '))
a = []
for i in range(0,n,1):
    a.append(input('Digite um valor: '))
for i in range(0,n,1):
    if int(a[i]) % 2 == 0:
        print(a[i])
'''
'''a = [8.0 , 5.0 , 10.0 , 5.0]
print(a)
print(len(a))
a.append(0.0)
print(len(a))
for i in range(len(a)-1, 0 , -1):
    if i ==1:
        a[1] = 2.0
    else:
        a[i] = a[i-1]
print(a)
print(len(a))
'''
'''
a = []
for i in range(1,5,1):
    a.append(float(input('Digite o elemento: ')))
print(a)
print(sum(a))
print(len(a))
del a[1]
print(' a é igual: ', a)
print(len(a))
'''
'''
a = []
for i in range(1,11,1):
    a.append(float(input('Digite o elemento: ')))
print(a)
for i in range(9, -1, -1):
    print(a[i])
'''

'''
while(True):
    n = int(input('DIgite o número de notas: '))
    if n > 0:
        break
notas = []
for i in range(0,n,1):
    notas.append(float(input('Digite a nota%d: ' %(i+1))))
media = 0
for i in range(0,n,1):
    media += notas[i]/n
print(notas)
print(media)
'''
'''
from minha_bib import primo
n = int(input('Digite n: '))
if primo(n):
    print('Primo')
else: 
    print('Não é primo ')
'''
#exercício 15
'''
n = int(input('Digite o valor de n: '))
if n > 9999999 and n <=99999999:
    soma = 0
    while(n!=0):
        resto = n%10
        n = (n-resto)//10
        soma = soma + resto
    print(soma)
else:
    print('Não Sei')
'''
#exercício 16
'''
while(True):
    t1 = int(input('Digite o número de tomadas da T1: '))
    t2 = int(input('Digite o número de tomadas da T2: '))
    t3 = int(input('Digite o número de tomadas da T3: '))
    t4 = int(input('Digite o número de tomadas da T4: '))
    if t1 > 0 and t2 > 0 and t3 > 0 and t4 > 0:
        n = t1 + (t2-1) + (t3-1) + (t4-1)
        print(n)
        break
    else:
        print("O NÚMERO DE TOMADAS TEM QUE SER MAIOR QUE 0, DIGITE NOVAMENTE\n")
'''

#Exercício 17
'''
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
d = int(input('Digite o quarto número: '))
if a > b and b < c and c > d:
    print('S')
elif a < b and b > c and c > d:
    print('S')
elif c > b and c > d and a < b:
    print('S')
elif d > c and c > b and b > a:
    print('S')


elif a > b and b == c and c == d:
    print('S')
elif a > b and b < c and c == d:
    print('S')
    
elif b > a and b > c and c == d:
    print('S')

elif c > b and c > d and a == b:
    print('S')

elif d > c and b == c and  b == a:
    print('S')
elif d > c and c < b and a == b:
    print('S')

else:
    print('N')
'''

#Exercício 20
'''
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

for i in range(1000000,0,-1):
    if a%i == 0 and b%i == 0:
        print(i)
        break
'''

#Exercício 21
'''
n = int(input('Digite n: '))
a = int(input('Digite a: '))
b = int(input('Digite b: '))
i = 2
while i <= n+1:
    if i%a!=0 and i%b!=0:
        n = n+1
    if i%a == 0 or i%b == 0:
        print(i)
    i = i +1
'''    
#Exercício 22
'''
while(True):
    p = int(input(' Digite p: '))
    q = int(input(' Digite q: '))
    if q >= p :
        break
if str(p) in str(q):
    print('S')
else:
    print('N')
'''
#Fatorial
'''
while(True):
    while(True):
        n = int(input('Digite um numero positivo: '))
        if n >=0:
            break
    f = 1
    for i in range(2,n+1,1):
        f = f*i
    print('%d!=%d' %(n,f))
    opt = input('deseja continuar? [S ou N]')
    if opt == 'N':
        print('\n\nATE BREVE!')
        break
'''
