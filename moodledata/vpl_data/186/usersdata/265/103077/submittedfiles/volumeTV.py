V=int(input('digite o volume inicial: '))
T=int(input('digite a quantidade de trocas: '))
for i in range (0,T,1):
    A_i=int(input('digite as trocas de volume: '))
    if V+A_i>100:
        VT=100
    elif V+A_i<0:
        VT=0
    else:
        VT=V+A_i
print(VT)