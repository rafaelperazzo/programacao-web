# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#Pediremos ao usuário para fornecer  um número real de 4 dígitos para testarmos se o mesmo é ou não um número vampiro.
n=int(input('Digite um numero de 4 digitios:'))
#Criaremos uma lista vazia para incluir os dígitos do número e facilitar o seu acesso indivdual.
lista=[]
#Usaremos uma variável, que receberá o valor de "n" pois este será usado posteriormente.
z=n
#Criaremos uma repetição para anexar os valores de cada dígito de "n" na lista criada anteriormente.
while z>0:
    valor=z%10
    z=z//10
    #Utilizamos o comando insert(0,valor) para que a lista apresente a mesma ordem do numero. Ex:(1260 fica[1,2,6,0])
    lista.insert(0,valor)
##Agora temos os digitos do número a ser testado, anexado em uma lista, cada um representado por um índice diferente.
#Definimos uma função para saber se o número é ou não vampiro.
#A função testa se a multiplicação de uma combinação  
def vampiro(lista):
    if ((lista[0]*10)+lista[1])*((lista[2]*10)+lista[3])==n:
        return True
    elif ((lista[0]*10)+lista[1])*((lista[3]*10)+lista[2])==n:
        return True
    elif ((lista[1]*10)+lista[0])*((lista[2]*10)+lista[3])==n:
        return True
    elif ((lista[1]*10)+lista[0])*((lista[3]*10)+lista[2])==n:
        return True
    elif ((lista[0]*10)+lista[2])*((lista[1]*10)+lista[3])==n:
        return True
    elif ((lista[0]*10)+lista[2])*((lista[3]*10)+lista[1])==n:
        return True
    elif ((lista[2]*10)+lista[0])*((lista[1]*10)+lista[3])==n:
        return True
    elif ((lista[2]*10)+lista[0])*((lista[3]*10)+lista[1])==n:
        return True
    elif ((lista[0]*10)+lista[3])*((lista[1]*10)+lista[2])==n:
        return True
    elif ((lista[0]*10)+lista[3])*((lista[2]*10)+lista[1])==n:
        return True
    elif ((lista[3]*10)+lista[0])*((lista[1]*10)+lista[2])==n:
        return True
    elif ((lista[3]*10)+lista[0])*((lista[2]*10)+lista[1])==n:
        return True
    #Se nenhum dos testes feitos anteriormente forem verdadeiros, o número não é vampiro!.     
    else:
        return False
if vampiro(lista)==True:
    print(n)
    print('o número apresentado é um número vampiro')
else:
    print(n)
    print('O número apresentado não é um número vampiro')
