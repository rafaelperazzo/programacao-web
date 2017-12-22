# -*- coding: utf-8 -*-


    


n = int(input('Digite a quantidade de elementos da lista: '))

a= []
for i in range (0,n,1):
    valor_a= float(input('Digite o elemento da lista: '))
    a.append (valor_a)
def pico(a):
    for i in range (0,len(a),1):
        if a[i]<a[i+1] and a[i]==a[i+2]:
            print('S')
        if a[i]== a[i+2]==a[i+4]==a[i+6] and a[i+1]==a[i+3]==a[i+5]:
            print('N')
        if a[i]<a[i+1]<a[i+2]<a[i+3] and a[i+3]>a[i+4]>a[i+5]>a[i+6]:
            print('S')
pico(a)