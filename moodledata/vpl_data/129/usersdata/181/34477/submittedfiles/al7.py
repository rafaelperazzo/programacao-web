n = int(input('digite o valor n:'))
contador = 0
soma = 0
for i in range (2,n,1):
    if n%i==0:
        contador = contador + 1
        print (i)
        soma = soma + 1 
        if soma==n:
            print ('perfeito')
else:
    print ('não perfeito')
    

