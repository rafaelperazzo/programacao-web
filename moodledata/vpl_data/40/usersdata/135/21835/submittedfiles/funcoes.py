
def cpi(m_termos):      #cpi=calculo valor aproximado m de pi
    pi=3
    i=1
    while i<=m_termos:
        k=i*2.0
        a=(4.0/(k*(k+1)*(k+2)))*((-1)**(i+1))
        pi=pi+a
        i=i+1
    return pi

def ft(numero):         #ft=fatorial
    fatorial=1
    while numero>0:
        fatorial=fatorial*numero
        numero=numero-1
    return fatorial

def ccos(z,epsilon):    #ccos=calculo de cos(z) limitado por epsilon
    cosx=1.0
    i=2
    j=1
    while(z**i)/ft(i)>=epsilon:
        a=(-1)**j
        cosx=cosx+a*((z**i)/ft(i))
        i=i+2
        j=j+1
    return cosx

def cra(m,epsilon):     #cra=calculo da razao aurea
    pi_considerado=cpi(m)/5
    aurea=2*ccos(pi_considerado,epsilon)
    return aurea
        