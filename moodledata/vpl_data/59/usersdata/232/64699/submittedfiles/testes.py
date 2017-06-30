# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
print('Bem Vindo! Esse programa tem a finalidade \nde identificar se um número é feliz ou não.')

#Primeiro definimos uma função para separar os dígitos do número a ser testado
def listaDigitos(n):
    d=[]
    while n>0:
        m=n%10
        d.append(m)
        #Veja que colocamos os dígitos em uma lista 'd' para facilitar a manipulação dos dígitos
        n=n//10
    d.reverse()
    #Com o 'reverse' organizamos os dígitos de forma que ele fique na mesma ordem que está no número inicial
    return(d)

#Agora faremos uma função para somar os quadrados dos números
#Note que utilizamos como parâmetro da função a lista 'd' obtida com a função anterior
def somaQuadrados(d):
    soma=0
    for i in range (0,len(d),1):
        soma=soma+(d[i]**2)
    return(soma)
#Aqui retornamos a soma final dos quadrados de todos os dígitos dos números

#Já na função 'feliz(n)' verificaremos se o número a ser testado é feliz ou não
def feliz(n):
    inicial=n
    #Will explica daqui pra baixo
    felicidade=bool(False)
    while felicidade==False:
        digitosN=listaDigitos(n)
        n1=somaQuadrados(digitosN)
        if n1==1:
            felicidade=True
            return(True)
        elif n1==4 or n1==16 or n1==37 or n1==58 or n1==89 or n1==145 or n1==42 or n1==20:
            felicidade=True
            return(False)
            break
        n=n1
        
resposta=str('Sim')
while resposta=='Sim':
    n=int(input('\nPor favor insira o número a ser testado: '))
    if feliz(n):
        print('O número '+str(n)+' é feliz!')
    else:
        print('O número '+str(n)+' não é feliz!')
    resposta=str(input('\nDeseja continuar? Caso queira, digite "Sim". Caso contrário, digite "Não": \n'))
    if resposta=='Não':
        print('\nObrigado por utilizar nosso programa! :D')