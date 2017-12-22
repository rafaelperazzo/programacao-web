n = int(input("Digite um valor: "))
numeros=[]
for i in range (0,n,1):
    numeros.append(float(input("Digite o número%.d: " %(i+1))))
soma=0
for i in range (0,n,1):
    soma+=numeros[i]
media=soma/n
somatorio=0
for i in range (0,n,1):
    somatorio+=(numeros[i]-media)**2
desvPad=((1/(n-1))*somatorio)**(1/2)
        
    
    