# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos de cada matriz: '))
lista1=[]
lista2=[]
lista3=[]
for i in range (0,n,1):
    lista1.append(int(input('Digite o elemento%.d da lista1: ' %(i+1))))
for i in range (0,n,1):
    lista2.append(int(input('Digite o elemento%.d da lista2: ' %(i+1))))
for i in range (0,n,1):
    lista3.append(int(input('Digite o elemento%.d da lista3: ' %(i+1))))
'''É crescente? lista1'''
cont_c1=0
for i in range (0,n,1):
    if i+1<n:
        if lista1[i]<lista1[i+1]:
            continue
        else:
            cont_c1+=1
if cont_c1==0:
    print('S')
else:
    print('N')
'''É decrescente? lista1'''
cont_d1=0
for i in range (0,n,1):
    if i+1<n:
        if lista1[i]>lista1[i+1]:
            continue
        else:
            cont_d1+=1
if cont_d1==0:
    print('S')
else:
    print('N')
'''Possui elementos consecutivos iguais? lista1'''
cont_ci1=0
for i in range (0,n,1):
    if i+1<n:
        if lista1[i]==lista1[i+1]:
            cont_ci1+=1
        else:
            continue
if cont_ci1==0:
    print('N')
else:
    print('S')
'''É crescente? lista2'''
cont_c2=0
for i in range (0,n,1):
    if i+1<n:
        if lista2[i]<lista2[i+1]:
            continue
        else:
            cont_c2+=1
if cont_c2==0:
    print('S')
else:
    print('N')
'''É decrescente? lista2'''
cont_d2=0
for i in range (0,n,1):
    if i+1<n:
        if lista2[i]>lista2[i+1]:
            continue
        else:
            cont_d2+=1
if cont_d2==0:
    print('S')
else:
    print('N')
'''Possui elementos consecutivos iguais? lista2'''
cont_ci2=0
for i in range (0,n,1):
    if i+1<n:
        if lista2[i]==lista2[i+1]:
            cont_ci2+=1
        else:
            continue
if cont_ci2==0:
    print('N')
else:
    print('S')
'''É crescente? lista3'''
cont_c3=0
for i in range (0,n,1):
    if i+1<n:
        if lista3[i]<lista3[i+1]:
            continue
        else:
            cont_c3+=1
if cont_c3==0:
    print('S')
else:
    print('N')
'''É decrescente? lista3'''
cont_d3=0
for i in range (0,n,1):
    if i+1<n:
        if lista3[i]>lista3[i+1]:
            continue
        else:
            cont_d3+=1
if cont_d3==0:
    print('S')
else:
    print('N')
'''Possui elementos consecutivos iguais? lista3'''
cont_ci3=0
for i in range (0,n,1):
    if i+1<n:
        if lista3[i]==lista3[i+1]:
            cont_ci3+=1
        else:
            continue
if cont_ci3==0:
    print('N')
else:
    print('S')