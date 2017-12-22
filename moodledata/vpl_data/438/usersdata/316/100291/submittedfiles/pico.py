# -*- coding: utf-8 -*-
def main():
    n=int(input('digite o numero de elementos: '))
    subiu=false
    desceu=false
    subiu_novamente=false
    anterior=int(input('digite um numero: '))
    atual=int(input('digite um numero: '))
    i=2
    if anterior<atual:
        subiu=true
    while i<n and anterior<atual:
        anterior=atual
        atual=int(input('digite um numero: '))
        i+=1
    if anterior<atual:
        desceu=true
    while i<n and anterior>atual:
        anterior=atual
        atual=int(input('digite um numero: '))
        i+=1
    if anterior<atual:
        subiu_novamente=true
    while i<n:
        atual=int(input('digite um numero: '))
        i+=1
    if subiu and desceu and not subiu_novamente:
        print('S')
    else:
        print('N')
print('N')