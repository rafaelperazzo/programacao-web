n = int(input('digite o valor n:'))
contador = 0
soma = 0
for i in range (2,n,1):
    if n%i==0:
        soma = soma + i
        contador = contador + 1
        print (i)
        if soma==n:
            print ('perfeito')
else:
    print ('não perfeito')
    

