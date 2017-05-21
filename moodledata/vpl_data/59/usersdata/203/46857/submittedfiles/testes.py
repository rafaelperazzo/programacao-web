n=int(input('digite n: '))
a=int(input('digite a: '))
b=int(input('digite b: '))
def simpson (a,b,n):
    h=(b-a)/n
    soma=0
    j=1
    i=a+j*h
    while i<=(b-h):
        if j%2!=0:
            soma=soma+4*(i**3-8*i+1)
        else:
            soma=soma+2*(i**3-8*i+1)
        j=j+1
        i=a+j*h
    soma=soma+(a**3-8*a+1)+(b**3-8*b+1)
    soma=(h/3)*soma
    return (soma)

    