v=int(input('Digite o volume inicial:'))
t=int(input('Digite o número de trocas:'))
soma=0
for i in range(1,t+1,1):
    x=int(input('Digite o novo valor:'))
    soma=v+x
    if soma>=100:
        soma=100
    if soma<=0:
        soma=0
    else: 
        soma=soma
    v=soma
print(soma)    