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
linha=0
M=0
#encontro a linha com erro
for i in range(2,n,1):
    if somalinha[i-2]==somalinha[i-1]:
        M=somalinha[i-2]
        continue
    elif somalinha[i-2]!=somalinha[i-1]:
        if somalinha[i-2]==somalinha[i]:
            M=somalinha[i-2]
            linha=i-1
            break
        elif somalinha[i-1]==somalinha[i]:
            M=somalinha[i-1]
            linha=i-2
            break
#se for a ultima linha
if somalinha[n-1]!=somalinha[n-2]:
    M=somalinha[n-2]
    linha=n-1
#encontro a coluna com erro
coluna=0
for i in range(2,n,1):
    if somacoluna[i-2]==somacoluna[i-1]:
        M=somacoluna[i-2]
        continue
    elif somacoluna[i-2]!=somacoluna[i-1]:
        if somacoluna[i-2]==somacoluna[i]:
            M=somacoluna[i-2]
            coluna=i-1
            break
        elif somalinha[i-1]==somalinha[i]:
            M=somacoluna[i-1]
            coluna=i-2
            break
#se for a ultima coluna
if somacoluna[n-1]!=somacoluna[n-2]:
    M=somacoluna[n-2]
    coluna=n-1
#encontro o tamanho do erro
tamanho=M-sum(m[linha])
print(m[linha][coluna]+tamanho)
print(m[linha][coluna])