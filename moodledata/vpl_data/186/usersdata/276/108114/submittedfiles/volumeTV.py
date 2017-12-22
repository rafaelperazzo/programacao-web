V = int(input ('Digite o volume inicial: '))
T = int(input ('Digite a quantidade de mudanças: '))

a = []

for i in range (0, T, 1):
    volume = int (input('Digite o volume: '))
    a. append (volume)
    
soma = V

for i in range (0,T,1):
    soma = soma + a[i]
    if soma >= 100:
        soma = 100
    
print (soma)