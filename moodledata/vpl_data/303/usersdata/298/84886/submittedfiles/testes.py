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
        while t3<=3:
            t3=int(input('Entrada inválida. Digite o número de tomadas da régua 3: '))
        if t3>1:
            while t4<=1:
                t4=int(input('Entrada inválida. Digite o número de tomadas da régua 4: '))
            if t4>1:
                k=(t1+t2+t3+t4)-3
                print(k)

#-----------------------------------------------------------------------------------------------------------------------------------

def algarismos(n):
    alg=1
    while (n//10)>0:
        n=n//10
        alg=alg+1
    return alg
    
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
def fatorial(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    return f

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