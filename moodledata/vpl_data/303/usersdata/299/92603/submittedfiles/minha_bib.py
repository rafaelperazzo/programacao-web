# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def sorteio(x,y):
    import random 
    sort=random.randint(0,1)
    if sort==1:
        return(0)
    else:
        return(1)

def sorteio2(x,y):
    import random 
    sort=random.randint(0,2)
    return(sort)
    
def mostrar_tabuleiro(l,c,v):
    linha=[0,0,0]
    linha1=[0,0,0]
    linha2=[0,0,0]
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
    return(print('',a,'|',b,'|',j,'\n',d,'|',e,'|',f,'\n',g,'|',h,'|',i))
    
