V=int(input('Informe o volume inicial:'))
T=int(input('Informe o número de trocas de volume:'))
for i in range(1,1+T,1):
    a=int(input('Informe a modificação do volume:'))
    V=V+a
    if V<0:
        V=0
    if V>100:
        V=100
print(V)    
    