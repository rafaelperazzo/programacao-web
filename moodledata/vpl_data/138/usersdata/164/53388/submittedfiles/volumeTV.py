v=int(input('Digite o volume inicial: '))
t=int(input('Digite quantas vezes houve a troca de volume: '))
volume=v
cont=0
for i in range (1, t+1, 1):
    a=int(input('Digite a modificação do volume: '))
    volume=volume+a
print(volume)        