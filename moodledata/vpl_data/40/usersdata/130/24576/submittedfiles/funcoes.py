#ARQUIVO COM SUAS FUNCOES
def absoluto(x):
    if x<0:
        x=x*(-1)
        resultado=x
        return resultado
def pi:
    m=input('Digite o numero m de termos da formula de pi:')
    So=3
    a=2
    for i in range(1,m+1,1):
        if (a//2)%2==0:
           So=So-4/(a*(a+1)*(a+2))
        else:
           So=So+4/(a*(a+1)*(a+2))
        a=a+2
pi=So