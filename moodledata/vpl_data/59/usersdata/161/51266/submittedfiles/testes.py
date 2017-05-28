lista=[]
n=int(input('n:'))
soma=0
for i in range(1,n+1,1):
    numero=int(input('numero:'))
    lista.append(numero)
for termo  in range(1,len(lista),1):
    soma=soma+lista[termo]
media=soma/len(lista)
print(media)
print(lista)    