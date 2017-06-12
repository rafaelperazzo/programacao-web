n=int(input('digite n:'))
denominador=2
soma=0
for i in range(1,n+1,1):
    soma=soma+1/denominador
    denominador=denominador+2
print(soma)