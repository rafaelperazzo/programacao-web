#ARQUIVO COM SUAS FUNCOES

def pi(a):
    pii=0
    c=-1 # c controla o sinal da função
    j=2    
    for i in range(0,a,1):
        b=(4/(j*(j+1)*(j+2)))
        c=(c*(-1))
        b=(b*c)
        pii=pii+b
        j=j+2
    pii=pii+3
    return pii