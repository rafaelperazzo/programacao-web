n=int(input('digite um numero: '))
i=2
contador=0
while (i<(n-1)):    
    if n%2==0:  
        contador=contador+1
    i=i+1
if contador>0:
    print('%d nao eh primo' %n)
else:
    print('%d é primo' %n)
    