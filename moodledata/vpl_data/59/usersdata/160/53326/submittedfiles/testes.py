def media(n):
    soma=0
    for i in range(0,len(n),1):
        soma=soma+n[i]
    resultado=soma/len(n)
    return(resultado)
    
n=int(input('Digite a quantidade de de elementos da lista:'))
a=[]
for i in range(0,n,1):
    valor=int(input('Digite os elementos da lista:'))
    a.append(valor)


print(a[0])
#print da media aritmetica
print (media(a))
