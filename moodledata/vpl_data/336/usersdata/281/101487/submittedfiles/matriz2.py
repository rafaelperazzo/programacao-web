# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite a dimensão da matriz: '))
m=np.empty([n,n])
for i in range (0,n,1):
    for j in range (0,n,1):
        m[i][j] = float(input('Digite o elemento da linha %de coluna %d: ' %(i,j)))
somaLinha=0
somaColuna=0
somaDPrincipal=0
somaDSecundaria=0
for i in range (0,n,1):
    for j in range (0,n,1):
        somaLinha+=m[i][j]
    somaLinha*=-1
for j in range (0,n,1):
    for i in range (0,n,1):
        somaColuna+=m[i][j]
    somaColuna*=-1
for i in range (0,n,1):
    if i<(n-1):
        if m[i][i]==m[i+1][i+1]:
            somaDPrincipal+=m[i][i]
            somaDPrincipal*=-1
for i in range (0,n,1):
    if i<(n-1):
        if m[i][i]!=m[i+1][i+1]:
            somaDPrincipal+=m[i][í]
        if i==(n-1):
            somaDPrincipal+=m[i][i]
            somaDPrincipal*=-1
for i in range (0,n,1):
    for j in range (0,n,1):
        somaDSecundaria+=m[i][j]
    somaDSecundaria*=-1
if somaLinha==somaColuna and somaLinha==somaDPrincipal and somaLinha==somaDSecundaria:
    print('S')
if somaLinha!=somaColuna and somaLinha!=somaDPrincipal and somaLinha!=somaDSecundaria:
    print('N')
