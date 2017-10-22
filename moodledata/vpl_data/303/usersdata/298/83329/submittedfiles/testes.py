def fatorial(n):
    i=1
    j=1
    while i<n:
        j=j*i
        i=i+1
        j=j+1
    return i

n = int(input('Digite um número inteiro não-negativo: '))
while n<0:
    print('Entrada inválida')
    n = int(input('Digite um número inteiro não-negativo: '))
if n==0:
    print('0! = 1')
if n==1:
    print('1! = 1')
while n>1:
    k = fatorial(n)
    print('%i = %i' % (n,k))