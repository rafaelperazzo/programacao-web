v=int(input('Digite o volume inicial: '))
t=int(input('Digite quantas vezes houve a troca de volume: '))
volume=0
cont=0
for i in range (1, t+1, 1):
    a=int(input('Digite a modificação do volume: '))
    volume=v+a
    while (0<volume<100):
        cont=cont+1
if (cont>0):
    print(volume)        