#ARQUIVO COM SUAS FUNCOES

def pi(m):
    
    den=2
    sinal=1
    soma=3
    '''
    'den' é a variável usada para controlar o valor dos termos do denominador.
    
    A variável 'sinal' é usada para controlar o sinal de cada termo.
    
    A soma começa em 3 para que não seja preciso adicionar 3 no final, pois 
    já é o primeiro valor do somatório.
    '''
    
    for i in range (0,m,1):
        soma=soma+((4/(den*(den+1)*(den+2)))*sinal)
        den=den+2
        sinal=sinal*(-1)
    
    return soma


def fatorial(x):
    
    fatorial=1
    for i in range(x,0,-1):
        fatorial=fatorial*i
        
    return fatorial


def valorAbsoluto(x):
    if x>=0:
        return x
    else:
        return x*(-1)

def co_seno(z,epsilon):
    
    d=2
    soma=1
    sinal=-1
    '''
    'd' é a variável usada para controlar o valor do denominador
     e nesse caso também é usada como controle do expoente.
     
    'soma' começa em 1, pois já é o primeiro valor do somatório.
    
    'sinal' altera o sinal a cada termo.
    '''
    while True:
        
        termo=((z**d)/funcoes.fatorial(d))*sinal

        if funcoes.valorAbsoluto(termo)<=epsilon:
            break
        
        soma=soma+termo
        sinal=sinal*(-1)
        d=d+2
        
    return soma
    
def razaoAurea(m,epsilon):
    
    x=funcoes.pi(m)/5
    resultado=funcoes.co_seno(x,epsilon)*2
    
    return resultado


