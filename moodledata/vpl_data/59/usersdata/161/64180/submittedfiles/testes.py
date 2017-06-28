m=int(input('Digite o número m de termos da fórmula pi:'))
x=float(input('a'))
def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return (x)

def calcula_pi(m):
    pi=3
    y=2
    for i in range(1,m+1,1):
        if i%2==0:
            pi=pi-((4)/(y*(y+1)*(y+2)))
        else:
            pi=pi+((4)/(y*(y+1)*(y+2)))
        y=y+2
    return(pi)
    
z= calcula_pi(m)   
print('%.15f' %z)        
    
print(calcula_valor_absoluto(x))