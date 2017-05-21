a=int(input('a:'))
soma=0
numerador=1
denominador=1
for i in range(1,a+1,1):
    if i%2!=0:
        soma=soma+(numerador/denominador)
    if 1%2==0:
        soma=soma-(numerador/denominador)
    numerador=numerador+1
    denominador=numerador**2
print('%.5f' %soma)

