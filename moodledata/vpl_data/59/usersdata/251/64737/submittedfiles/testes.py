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


#Aqui, definimos uma função, que recebe o número digitado como parâmetro e através da interação
#com as funções anteriormente criadas, verifica se o número é feliz, ou não
#retornando verdadeiro, ou falso.
def feliz(n):
#Foi defininida uma variável lógica, afim de controlar a repetição    
    felicidade=bool(False)
    while felicidade==False:
#Foram definidas duas variáveis, para receber os resultados das funçôes: "listaDigitos" e "somaQuadrados"      
        digitosN=listaDigitos(n)
        n1=somaQuadrados(digitosN)
        if n1==1:
            felicidade=True
            return(True)
#Esses números específicos no caso contrário, são assim definidos, pois por definição
#todo número infeliz repete infinitamente o ciclo destes valores
        elif n1==4 or n1==16 or n1==37 or n1==58 or n1==89 or n1==145 or n1==42 or n1==20:
            felicidade=True
            return(False)
        n=n1    

#Aqui foi definida uma variável do tipo String, para o controle da repetição principal do programa        
resposta=str('Sim')
#Dentro desta repetição, o programa é executado e ao final de cada ciclo, é pedido uma confirmação do usuário
#para que o programa inicie outro ciclo, ou encerre a sua execução
while resposta=='Sim':
    n=int(input('\nPor favor insira o número a ser testado: '))
    if feliz(n):
        print('O número '+str(n)+' é feliz!')
    else:
        print('O número '+str(n)+' não é feliz!')
    resposta=str(input('\nDeseja continuar? Caso queira, digite "Sim", caso contrário, digite "Não": \n'))
    if resposta=='Não':
        print('\nObrigado por utilizar nosso programa! :D')

