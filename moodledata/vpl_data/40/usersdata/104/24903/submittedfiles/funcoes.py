def fatorial(n):
    f=1
    for i in range(0,n+1,1):
        n=f*i
    return n

print fatorial(3)