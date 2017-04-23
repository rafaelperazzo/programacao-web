n = int(input('digite o valor n:'))
contador = 0
for i in range (2,n,1):
    if n%i==0:
        contador == contador+1
        print (i)
        print ('nao primo')
    if contador == 0:
        print('primo')


