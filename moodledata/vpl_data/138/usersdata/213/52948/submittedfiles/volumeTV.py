
v=int(input('Informe o volume inicial: '))
t=int(input('Informe o número de trocas de volume: '))
 
for i in range(1,t+1,1):
    modificacao=int(input('Informe a quantidade de vezes que se apertou o botão: '))
    if (modificacao+v)>100:
        v=100
    elif (modificacao+v)<0:
        v=0
    else:
        v=v+modificacao

print(v)