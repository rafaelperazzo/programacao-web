v=int(input('volume inicial'))
t=int(input('apertadas no botão'))
soma=v
for i in range(1,t+1,1):
    n=int(input('botao apertadp'))
    soma=soma+n
print(soma)