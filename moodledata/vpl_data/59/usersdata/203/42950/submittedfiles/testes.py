n=int(input('digite n: '))
for numero in range(3,n+1,1):
    cont=0
    for divisor in range(2,numero,1):
        if numero%divisor==0:
            cont=cont+1
    if cont==0:
        print(numero)