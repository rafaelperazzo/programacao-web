n=int(input('numero:'))
soma=0
for i in range(0,n+1,1):
    fat=1
    for a in range(1,i+1,1):
        fat=fat*a
    soma=soma+(1/math.factorial)    
print(soma)    
   