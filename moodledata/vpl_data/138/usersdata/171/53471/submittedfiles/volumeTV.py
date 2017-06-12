vi=int(input('digite o volume inicial:'))
n=int(input('digite o numero de troca de volume:'))
soma=vi
for i in range(1,n+1,1):
    x=int(input('digite o numero de vezes que o botao foi pressionado:'))
        soma=soma+x
        if soma>100:
            soma=100
        elif soma<0:
            soma=0
print(soma)