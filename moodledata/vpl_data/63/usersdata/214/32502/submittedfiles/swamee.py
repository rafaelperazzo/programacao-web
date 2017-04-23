
f =float (input('Valor de f:'))
L= float(input('valor de l:'))
Q =float (input('Valor de Q:'))
DeltaH= float (input('Valor de DeltaH:'))
v= float (input('Valor de v:'))
g= 9.81
e= 0.000002
D=((8*f*L*Q**2)/(math.pi**2*g*DeltaH))**0.2
Rey= (4*Q)/(math.pi*D*v)
a= (E/(3.7*D))
b= (5.74/(Rey**0.9))
k=(0.25)/(math.log(a+b)**2)
print('%4f'%D)
print('%4f'%Rey)
print('%4f'%k)