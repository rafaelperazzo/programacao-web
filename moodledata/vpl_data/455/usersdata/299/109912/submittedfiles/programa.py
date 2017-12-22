# -*- coding: utf-8 -*-
n=int(input(''))
m=[]
for i in range(0,n,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(int(input('')))
    m.append(linha)
#somalinha
somalinha=[]
for i in range(0,n,1):
    soma=0
    for j in range(0,n,1):
        soma+=m[i][j]
    somalinha.append(soma)
#somacoluna
somacoluna=[]
for i in range(0,n,1):
    soma=0
    for j in range(0,n,1):
        soma+=m[j][i]
    somacoluna.append(soma)    
'''#soma diagonal principal
somadp=[]
for i in range(0,n,1):
    somadp+=m[i][i]
#soma diagonal sec
somadsec=[]
for i in range(0,n,1):
    somadsec+=m[i][i]'''
linha=0
M=0
for i in range(1,n,1):
    if somalinha[i-1]==somalinha[i]:
        M=somalinha[i-1]
        continue
    elif somalinha[i-1]!=somalinha[i]:
        if somalinha[i-1]==somalinha[i+1]:
            M=somalinha[i-1]
            linha=somalinha[i]
            break
        elif somalinha[i]==somalinha[i+1]:
            M=somalinha[i]
            linha=somalinha[i-1]
            break
coluna=0
for i in range(1,n,1):
    if somacoluna[i-1]==somacoluna[i]:
        M=somacoluna[i-1]
        continue
    elif somacoluna[i-1]!=somacoluna[i]:
        if somacoluna[i-1]==somacoluna[i+1]:
            M=somacoluna[i-1]
            coluna=i
            break
        elif somalinha[i]==somalinha[i+1]:
            M=somacoluna[i]
            coluna=i-1
            break
