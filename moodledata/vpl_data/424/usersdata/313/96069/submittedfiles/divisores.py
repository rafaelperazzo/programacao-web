# -*- coding: utf-8 -*-
n1 = int(input(' digite um numero:')
n2  = int(input('dgite outro numero:')

def encontramultiplos(a,b):
    i = 0
    multiplos = []
    while i <= n:
        if i % b == 0:
            multiplos.append(i)
            i = i + 1
        else:
            i = i + 1
        return multiplos

print( ' os multiplos de' ,n1,'e',n2 )        
        
