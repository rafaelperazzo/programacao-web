def f2(z):
    if z < 0:
        return (z*(-1))
    else:
        return z

z = f2(z) 









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
