 -*- coding: utf-8 -*-
vi=int(input('volume inicial da tela'))
torcas=int(input('número de trocas de volume feitas:'))
for i in range (0,trocas,1):
    nt=int(input('troca feita')
    vi=vi+nt
    if vi>100:
        vi=100
    elif vi<0:
        vi=0
print (vi)