n=int(input('digite n: '))
m=int(input('digite m: '))
ant=int(input('digite: '))
cont=0
for i in range(1,n,1):
    prox=int(input('digite: '))
    if ant-prox>m:
        cont=cont+1
    prox=ant
if cont!=0:
    print('N')
else:
    print('S')