n=127523
resto=n%10
n=n//10
soma=0
for i in range(1,n-1,1):
    soma=soma+resto*(2**i)
