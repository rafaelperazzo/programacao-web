# -*- coding: utf-8 -*-
from __future__ import division
    """ O programa, me Python, a seguir, consiste em calcular a razão áurea por meio do número de termos de π e por um valor para epsilon. """
    
def  calcula_valor_absoluto(x):
    #Quando o valor de x for menor que zero se faz necessário usá-lo em módulo, por isso faremos:
        if x<0:
            a = x*(-1)
            return a
        else:
            return x
    def calcula_pi(m):
         i = 2
         pi = 3
         cont = 1
         soma= 0
    # Para contador, iniciado em 1, for par a parte da função que calcula pi será multiplicada por -1, assim, pois alteramos os sinais na operação.
         while cont<= calcula_valor_absoluto(m):
             calpi = 4/(i*(i+1)*(i+2))
             if cont%2==0:
                 calpi = calpi*-1
             pi = pi+calpi
             i = i+2
             cont = cont +1
             soma = soma+calpi
         return pi  
         
    """Calculando o Cosseno"""
    """def calcula_co_so(z,epsilon): 
        epsilon=calcula_valor_absoluto(epsilon)
        cosseno=1
        cont=1
        n=2 
        while True:
            p=1
            for i in range(1,n+1,1): 
                p=p*i 
            cos1=(z**n)/p
            if cos1<epsilon: 
                break
            if cont%2!=0: 
                cos1=-cos1
            cosseno=cosseno+cos1
            n=n+2
            cont=cont+1
        return cosseno"""
    """Cálculo da razão áurea"""
    def calcula_co_so(z,epsilon):
        n = 2 #valor do primeiro expoente do numerador
        valorcos = 1
        cont =1
        epsilon =calcula_valor_absoluto (epsilon)#para que epsilon sempre assuma valores maiores que zero, sabendo que 0<epsilon<1
        while True:
            p = 1
            #fatorial dentro da repetição
            for i in range (1,n+1,1):
                p =p*i
            #Chamaremos essa parte de 'Cos1' , isso definirá a primeira parte do problema, abaixo o valor de z será elevado a primeira potencia (n=2) e dividido pelo p (que representa o fatorial de n)
            cos1 = (z**n)/p
            #sabe-se que cos1<epsilon que é a condição de break para essa função,logo:
            if cos1<epsilon:
                break
            # Nota-se que, atribuindo a variável cont = 1, sempre que essa for um valor impar o valor de Cos1 é negativo, desse modo:
            if cont%2!=0:
                cos1=-cos1
            valorcos =valorcos+cos1
    #Atualizações e suas devidas explicações:
            n = n+2
    #Tanto as potências como os fatoriais tem inicio no valor 2 e aumentam ao passo  = 2.
            cont  = cont +1
    #adicionando uma unidade ao contador a cada atualização pode-se calcular de forma alternada,entre valores positivos e negativos para cos1.
        return valorcos
    def calcula_razao_aurea(m, epsilon):
        ra =  2*calcula_co_so((calcula_pi(m)/5),epsilon)
        return ra
        
    m = input("Digite o numero m de termos da formula do Pi: ")
    epsilon = input("Digite o epsilon para o calculo da razao aurea: ")
    print ("Valor aproximado de Pi: %.15f" %funcoes.calcula_pi(m))
    print("Valor aproximado da Razao Áurea: %.15f" %funcoes.calcula_razao_aurea(m,epsilon))

   


