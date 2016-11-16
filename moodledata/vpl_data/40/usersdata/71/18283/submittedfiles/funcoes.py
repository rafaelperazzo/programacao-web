#Definir módulo de x
def modulo(x):
    if x<0:
        return -x
    else:
        return x

#Definir a forma de como calcular Pi, usando m termos da fórmula dada
def pi(m): 
    #atribuições
    m=modulo(m)
    pi = 3
    contador=1
    d=2 #primeiro termo do denominador
    #processamento
    while contador<=m:
        a=4/(d*(d+1)*(d+2))
        if contador%2==0:
            a=-a
        pi=pi+a
        #atualizações
        contador=contador+1
        d=d+2
    return pi
    
#Definir a forma de como calcular o cosseno de um número z, usando o critério de parada epsilon
def cosseno(z,epsilon): 
    #atribuições
    epsilon=modulo(epsilon)
    cos=1
    contador=1
    n=2 #potencia do numerador e o número que têm que ser calculado o fatorial, para o denominador
    #processamento
    while True:
        produto=1
        for i in range(1,n+1,1): #Cálculo do Fatorial de n
            produto=produto*i 
        pa=(z**n)/produto #resultado parcial do termo 
        if pa<epsilon: #critério de parada
            break
        if contador%2!=0: #verificar se o termo têm que ser + ou -
            pa=-pa
        cos=cos+pa
        #atualizações
        n=n+2
        contador=contador+1
    return cos

#Definir a forma de como calcular a razão áurea usando o m, para calcular o pi, e o epsilon, para calcular o cosseno
def razao_aurea(m,epsilon): 
    return 2*cosseno(pi(m)/5,epsilon)