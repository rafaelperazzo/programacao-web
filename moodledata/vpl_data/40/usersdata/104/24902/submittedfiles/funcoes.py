def fatorial(n):
    f=0
    for i in range(1,n-1,1):
       f=f+(n*i)
    return f  
print fatorial(3)