def fatorial(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    print('%d! = %d' % (n,k))
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
    k = fatorial(n)
