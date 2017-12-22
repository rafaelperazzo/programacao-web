n = int(input("Digite um valor: "))
numeros=[]
for i in range (0,n,1):
    numeros.append(float(input("Digite o número%.2f: " %(i+1))))
soma=0
for i in range (0,n,1):
    soma+=numeros[i]
media=soma/n
print(media)
        
    
    