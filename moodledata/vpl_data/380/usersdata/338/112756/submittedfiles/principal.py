n = int(input('digite a quantidade de elementos: '))
lista=[]
lista_par=[]
lista_impar=[]
for i in range(n):
    x = int(input('Digite os elementos: '))
    if x%2 == 0: 
        lista.append(x)
        lista_par.append(x)
    if x%2 == 1:
        lista.append(x)
        lista_impar.append(x)
        
print(sum(lista_impar))
print(sum(lista_par))
print(len(lista_impar))
print(len(lista_par))
print(lista)