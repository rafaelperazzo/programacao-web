# -*- coding: utf-8 -*-

def pico(a):
    c = 0
    for i in range (0,len(a)-1,1):
        if n[i]> n[i+1]:
            c+=1
    if c == len(a)-1:
        return True
    else:
        False

n = input('Digite a quantidade de elementos da lista: ')
l = []
p = 0
for i in range (0,n,1):
    l.append(int(input()))
for i in range (0,len(l)-1,1):
    if (l[i]>l[i+1]:
        p = 1
        break
if pico(l[p:len(l)]):
    print('S')
else:
    print('N')