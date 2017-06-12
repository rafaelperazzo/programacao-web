n=int(input('digite n:'))
soma=0
for i in range(1,n,1):
    if n%i==0:
        soma=soma+1
if soma==n:
    print('perfeito')
else:
    print('não perfeito')