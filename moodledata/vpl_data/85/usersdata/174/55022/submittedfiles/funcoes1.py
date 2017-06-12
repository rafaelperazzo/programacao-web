# -*- coding: utf-8 -*-

def crescente (lista):
    #código da função crescente
    for i in range(0,len(lista)-1,1):
        cont=0
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==(len(lista)):
        return True
    else:
        return False
def decrescente (lista):
    #código da função decrescente
    for i in range(0,len(lista)-1,1):
        cont=0
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==len(lista):
        return True
    else:
        return False
def consecutivos (lista):
    #código da função de elementos consecutivos
    for i in range(0,len(lista)-1,1):
        cont = 0
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont!=1:
        return True
    else:
        return False
        
#escreva as demais funções
# Pedir a quantidade de elementos das listas
n = int(input('Quantidade de elementos: '))
# Criar as listas vázias
a=[]
b=[]
c=[]
# Inserir elementos à lista
for i in range(1,n+1,1):
    a.append(input('Lista A - %dº Valor: '%i))
for i in range(1,n+1,1):
    a.append(input('Lista B - %dº Valor: '%i))
for i in range(1,n+1,1):
    a.append(input('Lista C - %dº Valor: '%i))

#escreva o programa principal
def testar(lista):
    # código da função para fazer os 3 testes
    if crescente(lista):
        print ('S')
    else:
        print ('N')
    if decrescente(lista):
        print ('S')
    else:
        print ('N')
    if consecutivos(lista):
        print ('S')
    else:
        print ('N')

# Imprimir os resultados
print (testar(a))
print (testar(b))
print (testar(c))