n=int(input('numero de competidores:'))
soma=3
x=2
for i in range(n,p+1,1):
   if i%2==0:
       soma=soma-(4/(x*(x+1)*(x+2)))
    if i%2!=0:
        soma=soma+(4/(x*(x+1)*(x+2)))
    x=x+2    
print(soma)