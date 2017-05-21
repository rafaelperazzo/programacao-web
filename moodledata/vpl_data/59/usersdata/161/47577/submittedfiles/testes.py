n=int(input('numero de competidores:'))
p=int(input('nota minima:'))
soma=0
for i in range(n,p+1,1):
   if i%2==0:
       soma=soma+1
print(soma)