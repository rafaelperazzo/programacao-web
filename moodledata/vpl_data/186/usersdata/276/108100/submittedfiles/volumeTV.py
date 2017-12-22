V = int(input ('Digite o volume inicial: '))
T = int(input ('Digite a quantidade de mudanças: '))

a = []

for i in range (0, T, 1):
    volume = int (input('Digite o volume: '))
    a.append (volume)
    

for i in range (0, T, 1):
    F = V + a[i]
    V = F
    
print (F)