a=int(input('Digite um numero:'))

soma=0
while p>=0:
    i=a//10
    r=a%10
    soma=soma+5
    a=a//10
if soma==1:
    print('Numero feliz')
else:
    print('Numero Infeliz)