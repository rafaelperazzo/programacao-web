n=int(input('n:'))
contador=0
for i in range (2,n,1):
    contador=contador+1
if contador==0:
    print('primo')
else:
    print('nao primo')