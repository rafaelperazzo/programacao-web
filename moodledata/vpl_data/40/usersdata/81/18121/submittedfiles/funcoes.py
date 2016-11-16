#ARQUIVO COM SUAS FUNCOES

def cos(e,fat):
    soma=0
    while 0<soma<=e:
        for j in range(1,e,1):
            for i in range(2,e,2):
                soma=soma+(((e**i)/fat(i))+((-1)**j))
            
def fat(numero):
    f=1
    while numero>1:
        f*=numero
        numero-=1
    return f
            


def razao(pi,cos):
    aurea=2*cos.(pi/5)
    return aurea
    
