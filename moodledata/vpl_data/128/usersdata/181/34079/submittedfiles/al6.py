n = float(input('digite o valor n:'))
contador = 0
i = 2
while n>i:
    if n%i==0:
        contador=contador+1
    i=i+1
if contador==0:
    print('primo')
else:
    print('não primo')
    

