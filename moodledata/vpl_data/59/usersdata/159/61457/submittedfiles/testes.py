# -*- coding: utf-8 -*-
def angulo (g,m,s):
    angulom=m/60
    angulos=s/360
    soma=g+angulom+angulos
     
    return soma

def graus (azi):
    a=np.zeros((len(azi),3))
    for i in range (0,len(azi),1):
        g=int(azi[i])
        b=azi[i]-g
        c=b*60
        m=int(c)
        j=c-m
        s=j*60
        a[i,1]=g
        a[i,2]=m
        a[i,3]=s
    return a    
    
def azimute (angulo,d):
    azi=[]
    for i in range (0,len(d),1):
        azimute=angulo+d[i]
        azi.append(azimute)
        angulo=azimute
        return (azi)
        

g=int(input('Graus do primeiro azimute:'))
m=int(input('Minutos do primeiro azimute:'))
s=int(input('Segundos do primeiro azimute:'))
n=int(input('Numéro de pontos'))

d=[]
for i in range (0,n,1):
    deflexao=float(input('Deflexão:'))
    d.append(deflexao)

primeiroazi=(angulo(g,m,s))

azimutes=azimute(primeiroazi,d)

print(graus(azimutes))


        
        
        