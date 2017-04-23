n=int(input('n:'))
contador=0
i=2
while 1<n:
    if n%i==0:
        contador=contador+1
    i=i+1
if contador==0:
    print('primo')
else:
    print('nao primo')