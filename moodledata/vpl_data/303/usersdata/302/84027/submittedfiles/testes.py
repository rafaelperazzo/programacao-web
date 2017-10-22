#Exercício 17
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

else:
    print('N')







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
