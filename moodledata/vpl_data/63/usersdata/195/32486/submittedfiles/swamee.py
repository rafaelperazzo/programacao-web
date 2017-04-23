f=float(input('Digite o valor de f:'))
l=float(input('Digite o valor de l:'))
q=float(input('Digite o valor de q:'))
DeltaH=float(input('digite o valor de DeltaH:'))
v=float(input('digite o valor de v:'))
g=9.81
e=0.000002
d=((8*f*l*q*q)/(math.pi*math.pi*g*DeltaH))**0.2
rey=(4*q)/(math.pi*d*v)
k=0.25/(math.log10((e/(3.7*d))+(5.74/(rey**0.9))))**2
print('valor d é: %.4f' %d)
print('valor rey é: %.4f' %rey)
print('valor k é: %.4f' %k)
