#-*- coding: utf-8 -*-
#from__future__import division

def fatorial(m):
    mfat=1
    for i in range (2,m+1,1):
        mfat=mfat*i
    return (mfat)
    
m=int(input('Digite o número de m termos da fórmula pi:'))
e=input('Digite o epsilon para o cosseno:')

if m<0:
    m=m*(-1)
    
def calculapi(m):
    soma_pi=0
    j=2
    for i in range(0,m,1):
        if i%2==0:
            soma_pi=soma_pi+(4/(j*(j+1)*(j+2)))
        else:
            soma_pi=soma_pi-(4/(j*(j+1)*(j+2)))
        j=j+2
    pi=3+soma_pi
    return(pi)
        
def calculaCosseno(pi):
    soma_cosseno=0
    i=1
    j=2
    a=(((pi/5)**j)/fatorial(j))
    while a>e:
        if i%2!=0:
            soma_cosseno=soma_cosseno+a
        else:
            soma_cosseno=soma_cosseno-a
        j=j+2
        i=i+2
    cosseno=1-soma_cosseno
    return(cosseno)
    
def calculaRazaoAurea(cosseno):
    razaoAurea=2*(calculaCosseno(pi))
    return(razaoAurea)
    
pi=calculapi(m)
cosseno=calculaCosseno(calculapi)
razaoAurea=calculaRazaoAurea(cosseno)

print('%.15f'%pi)
print('%.15f'%cosseno)