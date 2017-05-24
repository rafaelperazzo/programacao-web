n=int(input('numero:'))
soma=0
for i in range(0,n,1):
    n=n//2
    r=n%2
    soma=soma+r*(10**i)
print(soma)    
   