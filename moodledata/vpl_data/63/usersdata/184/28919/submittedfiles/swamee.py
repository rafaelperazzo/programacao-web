f=float(input('digite f:'))
l=float(input('digite l:'))
q=float(input('digite q:'))
deltaH=float(input('digite deltaH:'))
v=float(input('digite v:'))
g=9.81
e=0.000002
d=((8*f*l*q*q)/(math.pi*math.pi*g*deltaH))**0.2
rey=(4*q)/(math.pi*d*v)
k=0.25/(math.log10((e/(3.7*d))+(5.74/(rey**0.9))))**2
print=('o valor de d é:%.4f'%d)
print=('o valor de rey é:%.4f'%rey)
print=('o valor de k é:%.4f'%k)


