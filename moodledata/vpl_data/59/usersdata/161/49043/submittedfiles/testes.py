n=int(input('numero:'))
soma=0
for i in range(0,n,1):
    r=n%10
    n=n//10
    soma=soma+r*(2**i)    
print(soma)    
   