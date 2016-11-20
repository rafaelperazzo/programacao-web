#ARQUIVO COM SUAS FUNCOES
def pi(x):
    s=3
    m=1
    i1=2
    i2=3
    i3=4
    y=((4)/(i1*i2*i3))
    while(m<=x):
        if i3%4==0:
            s=s+y
        else:
            s=s-y
        i1=i1+2
        i2=i2+2
        i3=i3+2
        m=m+1
    return s    
    