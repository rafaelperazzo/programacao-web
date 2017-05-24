n=int(input('Digite n:'))
soma=1
denominador=1
for numerador in range(1,n+1,1):
    if numerador%2==0:
        denominador=denominador-(numerador**2)
    soma=soma+numerador/denominador    
    if numerador%2!=0:
        denominador=denominador+(numerador**2)
    soma=soma+numerador/denominador
print('%.5f' %soma)    
    
