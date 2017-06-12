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
    
def calcularPi(m):
    somapi=0
    j=2
    for i in range(0,m,1):
        if i%2==0:
            somapi=somapi+(4/(j*(j+1)*(j+2)))
        else:
            somapi=somapi-(4/(j*(j+1)*(j+2)))
        j=j+2
    pi=3+somapi
    return(pi)
        
def cosseno(pi):
    somacosseno=0
    i=1
    j=2
    a=(((pi/5)**j)/fatorial(j))
    while a>e:
        if i%2!=0:
            somacosseno=somacosseno+a
        else:
            somacosseno=somacosseno-a
        j=j+2
        i=i+2
    cosseno=1-somacosseno
    return(cosseno)
    
def razaoAurea(cosseno):
    RazaoAurea=2*(cosseno(pi))
    return(RazaoAurea)
    
pi=calcularpi(m)
cosseno=cosseno(calcularpi)
razaoaurea=razaoAurea(cosseno)

print('%.15f'%pi)
print('%.15f'%cosseno)