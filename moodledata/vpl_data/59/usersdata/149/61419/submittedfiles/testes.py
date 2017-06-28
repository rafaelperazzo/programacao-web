# -*- coding: utf-8 -*-
import itertools 
#número vampiro é um número onde a multiplicado de todas as combinações possiveis -os dois termos primeiro com os dois ultimos dê pelo menos
#uma combinação igual ao número dado...como é um exercício que se trata de permutação simples, tive que procurar um código que gerasse todas
#as combinações possíveis de uma lista...como o exercício pede para o usuário programar se é um número vampiro de 4 dígitos apenas, estimu
#lei logo o tamanho da lista igual 4 !!!


n=4
z=[]
for i in range(0,n,1):
    lista=int(input('digite o elemento do índice '+str(i)+' :'))
    z.append(lista)


#como o z é uma lista no formato (x,y,z,w), tranformei cada índice desta lista em texto com o comando STR e somei estes índices para ficar no
#formato (xyzw) e depois tranformei de novo para número com o comando INT fechando todo o código. Assim, podemos comparar este número todo com
#a multiplicação de todas as permutações possíveis e comparar se existe alguma multiplicação que seja igual a este número guardado na variável g.


g=int(str(z[0])+str(z[1])+str(z[2])+str(z[3]))


#código para a permutação da lista...além do código da linha 2....este código pega todos os índice da lista z e permuta todas as combinações
#possiveis para este número, ou seja 4!(fatorial)= 24 permutações.


permut=list(itertools.permutations(z))


#iniciei o contador para contar se há pelo menos UMA combinação onde a multiplicação dos 2 termos primeiros vezes os dois ultimos dê o número inicial...


cont=0


#como o exercício pede para programar um programa onde dado 4 números verificar se é vampiro... aplicando permutação simples sei que para 4 números 
#existe 24 permutações possíveis..por isso considerei logo os intervalo da repetição a seguir de 0 a 23. 


for i in range(0,23,1):


#como queria multiplicar os dois primeiros índices (0 e 1) pelos dois últimos (2 e 3), transformei essas duas partes do inicio e fim em textos com o STR
#e transformei em inteiro as mesmas para poder fazer a multiplicação delas e guardar essas multiplocações na variável p


    p=int(str(permut[i][0])+str(permut[i][1]))*int(str(permut[i][2])+str(permut[i][3]))


#para saber se exite pelo menos uma permutação onde a multiplicação desse igual ao número guardado na variável g, fiz a condição seguinte:   


    if p==g:
        cont=cont+1
if cont>=1:
    print('Sim, é um número vampiro')
else:
    print('Não é um número vampiro')


    

    
    
    
    
    
    
    
    

    