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


#dp
soma=((a)-media(a))**2
    
s=(1/((a)-1)*soma)**1/2


#print do primeiro elemento
print('%.2f'%a[0])

#print do ultimo elemento
print('%.2f'%(a[i]))

#print da media aritmetica
print ('%.2f'%media(a))

#print da lista
print(a)

