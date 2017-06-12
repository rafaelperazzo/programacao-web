n=int(input('digite n:'))
termo=1
denominador=1
soma=0
for i in range(1,n+1,1):
    soma=soma+termo/denominador
    denominador=termo*termo
print('%5.f'%soma)
