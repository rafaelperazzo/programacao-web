n=int(input('digite n: '))
for numero in range(3,n+1,1):
    soma=0
    for divisor in range(1,numero,1):
        if numero%divisor==0:
            soma=soma+divisor
    if soma==numero:
        print(numero)