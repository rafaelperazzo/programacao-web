#ARQUIVO COM SUAS FUNCOES
cpi(valor):              #cpi=calculo valor aproximado x de pi
    y=3
    i=1
    while i<=x:
        k=i*2.0
        a=(4.0/(k*(k+1)*(k+2)))
        b=(-1)**(i+1)
        y=y+a*b
        i=i+1
        
    return y

ft(numero):             #ft=fatorial
    k=1
    while numero>0:
        k=k*numero
        numero=numero-1
        
    return k

ccos(x,epsilon):        #ccos= calculo de cosseno x
    cosx=1.0
    i=2
    j=1
    while(x**i)/ft(i)>=epsilon:
        a=(-1)**j
        cosx=cosx+a*((x**i)/ft(i))
        i=i+2
        j=j+1
        
    return cosx