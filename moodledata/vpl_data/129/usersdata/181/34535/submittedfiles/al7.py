n = int(input('digite o valor n:'))
soma = 0
for i in range (2,n,1):
    if n%i==0:
        print (i)
soma = soma + i        
if soma == n:
    print ('perfeito')
else:
    print ('não perfeito')
    

