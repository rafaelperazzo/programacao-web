n=int(input('numero:'))
for numero in range(3,n+1,1):
    soma=0
    for divisor in range(1,numero,1):    
        if numero%divisor==0:
            soma=soma+1
    if soma==numero:
        print(numero)
 
   