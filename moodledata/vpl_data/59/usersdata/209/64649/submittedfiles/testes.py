# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#Primeiramente definiremos a função que determinará se o número é ou não um número vampiro!

def vampiro(x):
    
    #Criaremos uma lista para, em seguida, adicionar todos os elementos do número a ser analisado.
    #É preciso também armazenar o número em outra variável para poder ser utilizado posteriormente.
    
    a=[]
    y=x
    a.append(y//1000)
    y=y%1000
    a.append(y//100)
    y=y%100
    a.append(y//10)
    y=y%10
    a.append(y)
    
#Após criada a lista iremos analisar se é possivel escrever o número a ser analisado como uma multiplicação de dois pares de seus elementos.
#Exemplos: 1260=21*60 ou 1395=15*93
#Se for possível, a função retorná verdadeiro, caso não, retornará falsa.
#Testaremos utilizando condiões!
#Totaliza 12 possibilidades, tendo em vista a combinação de quatro para dois, que é 6, e como pode alternar a ordem do primeiro ou do segundo par, multiplicaremos duas vezes por 2!.
    
    if ((a[0]*10)+a[1])*((a[2]*10)+a[3])==x:
        return True 
    elif (a[0]*(10+a[1]))*(a[2]+(a[3]*10))==x:
        return True 
    elif (a[0]+(a[1]*10))*((a[2]*10)+a[3])==x:
        return True 
    elif (a[0]+a[1]*10)*(a[2]+(a[3]*10))==x:
        return True 
    elif (a[0]*10+a[2])*(a[1]*10+a[3])==x:
        return True 
    elif (a[0]*10+a[2])*(a[1]+a[3]*10)==x:
        return True 
    elif (a[0]+a[2]*10)*(a[1]*10+a[3])==x:
        return True 
    elif (a[0]+a[2]*10)*(a[1]+a[3]*10)==x:
        return True 
    elif (a[0]*10+a[3])*(a[1]*10+a[2])==x:
        return True 
    elif (a[0]*10+a[3])*(a[1]+a[2]*10)==x:
        return True 
    elif (a[0]+a[3]*10)*(a[1]*10+a[3])==x:
        return True 
    elif (a[0]+a[3]*10)*(a[1]+a[2]*10)==x:
        return True
    else:
        return False
        
#Após definirmos a função, é só pedir a entrada, que será o número a ser analisado!        
print('        ****************************************************************          ')
print('     Olá, este programa irá mostrar se um número com quatro algarismos é ou não um número vampiro!')
print('                    ')
Vamp=int(input('     Informar um valor a ser analisado:'))

#Então, utlizaremos a função criada para mostrar se o número informado na tela é vampiro ou não!

print(' ')
if vampiro(Vamp):
    print('     O número informado é vampiro!')
else:
    print('     O número informado não é vampiro!')
print(' ')
print('        ****************************************************************          ')
    
    
    
    
    
    
    
    
    
    
    
    