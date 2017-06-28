# -*- coding: utf-8 -*-

n=int(input('Digite o tamanho da sequência:'))
anterior=int(input('Digite um número:'))
maior_altura=0
i=1
while i<n:
    atual=int(input('Digite um número:'))
    i=i+1
    altura_degrau=atual-anterior
    if altura_degrau<0:
        altura_degrau= -altura_degrau
print