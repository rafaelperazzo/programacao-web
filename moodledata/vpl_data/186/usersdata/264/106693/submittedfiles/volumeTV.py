V= int(input('Digite o volume inicial:'))
T= int(input('Digite a quantidade de trocas:'))

for i in range (0,T,1):
    A_i= int(input('Digite a quantidade de trocas de volume:'))
    if V+A_i>100:
        V=100
    elif V+A_i<0:
        V=0
    else:
        V= V+A_i
print (V)
    