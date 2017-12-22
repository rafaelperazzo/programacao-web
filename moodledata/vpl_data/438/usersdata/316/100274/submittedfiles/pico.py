# -*- coding: utf-8 -*-
def main():
    n=int(input('digite o numero de elementos: '))
    anterior=int(input('digite um numero: '))
    atual=int(input('digite um numero: '))
    if anterior<atual:
        pico=true
        subida=true
    else:
        pico=false
    anterior=atual
    i=2
    while i<n:
        atual=int(input('digite um numero: '))
        if anterior<atual:
            if not subida:
                pico=false
        else:
            subida=false
        alterior=atual
        i+=1
    if subida:
        pico=false
    if pico:
        print('S')
    else:
        print('N')
main()