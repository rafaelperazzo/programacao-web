n=int(input('digite n:'))
cont=0
i=2
while i<n:
    if n%i==0:
        cont=cont+1
    i=i+1
if cont==0:
    print('primo')
else:
    print('não primo')
