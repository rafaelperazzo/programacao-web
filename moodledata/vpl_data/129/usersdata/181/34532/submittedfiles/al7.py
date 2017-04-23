n = int(input('digite o valor n:'))
soma = 0
for i in range (2,n,1):
    if n%i==0:
        soma = soma + i
        print (i)
if soma == n:
    print ('perfeito')
else:
    print ('não perfeito')
    

