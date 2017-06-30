# -*- coding: utf-8 -*-
while 0!=1:
    n=int(input("Digite o número: ")) # A variavel n recebe o número a ser testado
    
    def digitos (n): # A função 'digitos' recebe n, separa seus algarismos e os insere em uma lista
        a=[]
        while n>0:
            if n>=10:
                digito=n%10
                a.append(digito)
            else:
                a.append(n)
            n=n//10
        return(a)
        
    def feliz (a): # A função 'feliz' recebe a lista dos digitos de n e realiza as operações para descobrir se n é feliz ou não
        c=0
        for i in range(0,len(a),1):
            c=c+(a[i]**2)
        return(c)
        
    while 0!=1: # Aqui inicia o looping que realizará a operação da função 'feliz' o número de vezes que for necessário (nota-se que a repetição é infinita e para somente se 'n' for identificado com Feliz ou Não Feliz) 
        k=digitos(n)
        o=feliz(k)
        if o==1:
            print("Feliz") # Caso o número seja identifica como Feliz, a repetição para e a frase é exibida na tela
            break
        elif o==89: # Caso o número seja identificado como Não Feliz, a repetição para e a frase é exibida na tela
            print("Não Feliz")
            break
        else:
          n=0+o  #Case ele ainda nao seja identificado como nenhuma das atribuições, a varialvel 'n' é atualizada para um novo número (gerado pela função feliz), esse número será, a partir de agora, ultilizado nas operações