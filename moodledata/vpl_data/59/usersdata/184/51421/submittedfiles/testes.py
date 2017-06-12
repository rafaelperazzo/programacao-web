n=int(input('digite n:'))
cont=0
for i in range(2,n,1):
    if n%i==0:
        cont=cont+1
if cont==0:
    print('primo')
else:
    print('não primo')