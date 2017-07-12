# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
print('Bem Vindo! Este programa tem a finalidade \nde identificar se um número é feliz ou não.')

def listaDigitos(n):
    d=[]
    while n>0:
        m=n%10
        d.append(m)
        n=n//10
    d.reverse()
    return(d)
    
def somaQuadrados(d):
    soma=0
    for i in range(0,len(d),1):
        soma=soma+(d[i]**2)
    return(soma)

def feliz(n):
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
    resposta=str(input('\nDeseja continuar? Caso queira, digite "Sim", caso contrário, digite "Não": \n'))
    if resposta=='Não':
        print('\nObrigado por utilizar nosso programa! :D')

