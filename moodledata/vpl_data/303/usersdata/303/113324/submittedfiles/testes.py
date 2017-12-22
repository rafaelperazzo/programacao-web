# -*- coding: utf-8 -*#notas=[]
#for i in range(0,50,1):
 #   notas.append(float(input('DIGITE A NOTA%d[%d]:' %(i+1 , i))))
lista=[]
lista_par=[]
lista_impar=[]

n=int(input('Digite a quantidade de termos:'))

for i in range(0,n,1):
    lista.append(int(input('Digite um número:')))
    
for i in range(0,len(lista),1):
    if lista[i]%2==0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])
        
        
print(lista)
print(lista_par)
print(lista_impar)

    

    
    