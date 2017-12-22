V = int(input ('Digite o volume inicial: '))
T = int(input ('Digite a quantidade de mudanças: '))

a = []

for i in range (0, T, 1):
    volume = int (input('Digite o volume: '))
    a.append (volume)
    

for i in range (0, T, 1):
    Vf = V + a[i]
    V = Vf
    
print (Vf)