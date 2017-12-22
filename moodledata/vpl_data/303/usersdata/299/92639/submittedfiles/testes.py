linha=[0,1,2]
linha1=[0,1,2]
linha2=[0,1,2]
a=linha[0]
b=linha[1]
c=linha[2]
d=linha1[0]
e=linha1[1]
f=linha1[2]
g=linha2[0]
h=linha2[1]
k=linha2[2]


from minha_bib import sorteio



from minha_bib import sorteio2
v2=simbolo2=0
v=simbolo=input('qual simbolo vc deseja usar?')
if simbolo=='X' or simbolo=='x':
    simbolo2='O'
else:
    simbolo2='X'
    
if sorteio(0,1)==0:
    primeiro='Computador'
else:
    primeiro='Usuário'
    
print('Vencedor do sorteio para início do jogo: '+primeiro)
if primeiro=='Computador':
    i=sorteio2(0,2)
    j=sorteio2(0,2)
    if i==0:
        if j==0:
            a=v
        elif j==1:
            b=v
        elif j==2:
            c=v
    elif i==1: 
        if j==0:
            d=v
        elif j==1:
            e=v
        elif j==2:
            f=v
    elif i==2:
        if j==0:
            g=v
        elif j==1:
            h=v
        elif j==2: 
            k=v
    print('',a,'|',b,'|',c,'\n',d,'|',e,'|',f,'\n',g,'|',h,'|',k)


i=sorteio2(0,2)
j=sorteio2(0,2)
if i==0:
    if j==0:
        a=v2
    elif j==1:
        b=v2
    elif j==2:
        c=v2
elif i==1:
    if j==0:
        d=v2
    elif j==1:
        e=v2
    elif j==2:
        f=v2
elif i==2:
        if j==0:
            g=v2
        elif j=1:
            h=v2
        elif j==2: 
            k=v2
print('',a,'|',b,'|',c,'\n',d,'|',e,'|',f,'\n',g,'|',h,'|',k)

jogada=str(input('qual sua jogada?'))
i=int(jogada[0])
j=int(jogada[1])
if i==0:
    if j==0:
        a=v
    elif j==1:
        b=v
    elif j==2:
        c=v
elif i==1:
    if j==0:
        d=v
    elif j==1:
        e=v
    elif j==2:
        f=v
elif i==2:
        if j==0:
            g=v
        elif j==1:
            h=v
        elif j==2: 
            k=v
print('',a,'|',b,'|',c,'\n',d,'|',e,'|',f,'\n',g,'|',h,'|',k)


i=sorteio2(0,2)
j=sorteio2(0,2)
if i==0:
    if j==0:
        a=v2
    elif j==1:
        b=v2
    elif j==2:
        c=v2
elif i==1:
    if j==0:
        d=v2
    elif j==1:
        e=v2
    elif j==2:
        f=v2
elif i==2:
    if j==0:
        g=v2
    elif j==1:
        h=v2
    elif j==2: 
        k=v2
print('',a,'|',b,'|',c,'\n',d,'|',e,'|',f,'\n',g,'|',h,'|',k)