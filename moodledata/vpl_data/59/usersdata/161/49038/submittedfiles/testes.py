b=int(input('numero:'))
soma=0
x=b
for a in range(0,b+1,1):
    b=b//10
    n=b
    for i in range(1,n,1):
        x=x%10
        r=x
        soma=soma+r*(2**i)    
print(soma)    
   