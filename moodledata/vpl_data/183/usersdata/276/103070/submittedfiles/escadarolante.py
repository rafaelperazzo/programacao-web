# -*- coding: utf-8 -*-

N = int (input('Digite a quantidade de pessoas'))

tempos = []

for i in range (0,N,1):
    T = int (input('Digite o tempo que cada pessoa passou pelo sensor'))
    tempos.append (T)

total = 0
maior = []

for i in range (0,N,1):
    if i == 0 :
        primeiro = 10
        segundo = tempos[i+1] + 10
        if primeiro >= segundo:
            maior.append (primeiro)
        elif segundo>primeiro:
            maior.append (segundo)
    elif i == len(tempos):
        primeiro = tempos [len(tempos)-2] + 10
        segundo = tempos [len(tempos)-1] + 10
        if primeiro >= segundo:
            maior.append (primeiro)
        elif segundo>primeiro:
            maior.append (segundo)
    else: 
        primeiro = tempos[i-1] + 10
        segundo = tempos [i] + 10
        if primeiro >= segundo:
            maior.append (primeiro)
        elif segundo>primeiro:
            maior.append (segundo)

print (max (maior))

        