m=int(input('Digite o número m de termos da fórmula pi:'))
def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return (x)

def calcula_pi(m):
    pi=3
    m=2
    for i in range(0,n,1):
        if i%2==0:
            pi=pi-(4/m*(m+1)*(m+2))
        else:
            pi=pi+(4/m*(m+1)*(m+2))
        m=m+2

def calcula_co_seno(pi,epsilon):
    
print('%.15f' %calcula_pi(m))        
    
print(calcula_valor_absoluto(x))