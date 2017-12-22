V= int(input('Digite o volume inicial:'))
T= int(input('Digite a quantidade de trocas:'))

for i in range (0,T,1):
    A_i= int(input('Digite a quantidade de trocas de volume:'))
    if V+A_i>100:
        V=100
    if V+A_i<0:
        V=0
    if A_i>0:
        V= V+A_i
    if A_i<0:
        V= V-A_i
print (V)
    