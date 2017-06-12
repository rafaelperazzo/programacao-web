vi=int(input('digite o volume inicial:'))
n=int(input('digite o numero de troca de volume:'))
soma=vi
for i in range(1,n+1,1):
    x=int(input('digite o numero de vezes que o botao foi pressionado:'))
    if x>0:
        soma=soma+x
    elif x<0:
        soma=soma-x
print(soma)