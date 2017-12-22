# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def sorteio(x,y):
    import random 
    sort=random.randint(1,2)
    if sort==1:
        return('Computador')
    else:
        return('Usuário')
def mostrar_tabuleiro(l,c,v):
    linha=[0,1,2]
    linha1=[0,1,2]
    linha2=[0,1,2]
    a=linha[0]
    b=linha[1]
    j=linha[2]
    d=linha1[0]
    e=linha1[1]
    f=linha1[2]
    g=linha2[0]
    h=linha2[1]
    i=linha2[2]
    if l==0:
        if c==0:
            a=v
        elif c==1:
            b=v
        elif c==2:
            j=v
    elif l==1:
        if c==0:
            d=v
        elif c==1:
            e=v
        elif c==2:
            f=v
    elif l==2:
        if c==0:
            g=v
        elif c==1:
            h=v
        elif c==2: 
            i=v
    return('',a,'|',b,'|',j,'\n',d,'|',e,'|',f,'\n',g,'|',h,'|',i)
