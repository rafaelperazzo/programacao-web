n=float(input('digite n: '))
n=int(n)
i=0
soma=0
while n>0:
    m=n%10
    soma=soma+m*2**i
    n=n//10
    i=i+i
print(soma)