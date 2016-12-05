
# Calculo do valor absoluto
def CalcValorAbsoluto(m):
    if m<0:
        m=m*(-1)
    return m
        
# Fatorial 
def fatorial (m):
    m_fat=1
    for i in range(2,m+1,1):
       m_fat=m_fat*i
    
    return m_fat
    
#PI
def calculoDopi(m):
    somaPi=0
    j=2
    for i in range(0,m,1):
        if i%2==0:
            somaPi=somaPi+(4/(j*(j+1)*(j+2)))
        else:
            somaPi=somaPi-(4/(j*(j+1)*(j+2)))
        j=j+2
    PI=3+somaPi
    return PI
            

    
        
# calculo do cosseno > CCOS

def CCOS(z,e):
    somaCosseno=0
    i=1
    j=2
    x=(z**j)/fatorial(j)
    while x>e:
        x=(z**j)/fatorial(j)
        if i%2 !=0 :
            somaCosseno=somaCosseno + x
        else:
            somaCosseno=somaCosseno - x
        j=j+2
        i=i+1
    cos=1-somaCosseno
    
    return cos
    
# calculo da razaoaurea 

def CRA (m,e):
    PI= calculoDopi(m)
    cos= CCOS(PI/5,e)
    razaoaurea= cos * 2
    
    return razaoaurea 