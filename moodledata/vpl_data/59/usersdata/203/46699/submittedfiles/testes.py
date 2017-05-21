n=int(input('digite n: '))
soma=0
for numerador in range (1,n+1,1):
    if numerador%2==0:
        soma=soma-(numerador/(numerador**2))
    else:
        soma=soma+(numerador/(numerador**2))
print('%.5f'%soma)
    