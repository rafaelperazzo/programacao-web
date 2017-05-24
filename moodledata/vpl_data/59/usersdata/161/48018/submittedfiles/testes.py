n=int(input('numero de competidores:'))
soma=1
pi=0
deno=1
nume=2
for i in range(1,n+1,1):
    soma=soma*(nume/deno)
    if i%2==0:
       deno=deno+2
    if i%2!=0:  
        nume=nume+2
    pi=soma*2    
print(pi)