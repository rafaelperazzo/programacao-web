# -*- coding: utf-8 -*-

f=int(input('digite f: '))
g=[]
h=[]
contG=0
contH=0
for z in range (1, f+1, 1):
    valorG=float(input('valor da lista G: '))
    g.append(valorG)
for i in range (0, len(g), 1):
    if (i==0):
        if (g[i]>g[i+1]):
            contG=contG+1
    elif (i==len(g)-1):
         if (g[i]>g[i-1]):
             contG=contG+1
    else:
        if (g[i]>g[i+1] and g[i]>g[i-1]):
            contG=contG+1
for z in range (1, f+1, 1):
    valorH=float(input('valor da lista H: '))
    h.append(valorH)
for i in range (0, len(h), 1):
    if (i==0):
        if (h[i]>h[i+1]):
            contH=contH+1
        elif (i==len(h)-1):
            if (h[i]>h[i-1]):
                contH=contH+1
            else:
                if (h[i]>[i+1] and h[i]>h[i-1]):
                    contH=contH+1

if (contG==1):
    print('S')
else:
    print('N')
if (contH==1):
    print('S')
else:
    print('N')
    
    
    
    




















