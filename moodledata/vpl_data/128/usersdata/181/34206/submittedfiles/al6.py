n = float(input('digite o valor n:'))
contador = 0
i = 2
d = n/i
while n>i:
    if n%i==0:
        contador=contador+1
    i=i+1
if d!=1 and d!=n:
    print('%f'%d)
else:
    print ('primo')
    

