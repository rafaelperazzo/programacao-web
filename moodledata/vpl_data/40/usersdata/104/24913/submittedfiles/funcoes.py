def fatorial(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    return f

print fatorial(6)