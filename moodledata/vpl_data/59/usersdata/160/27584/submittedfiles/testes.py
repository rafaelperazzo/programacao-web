

f=float(input('Digite um valor para f:'))
L=float(input('Digite um valor para L:'))
Q=float(input('Digite um valor para Q:'))
DeltaH=float(input('Digite um valor para DeltaH:'))
v=float(input('Digite um valor para v:'))

g=9.81
e=0.000002
D=(8*f*L*(Q*Q)/((math.pi*math.pi)*g*DeltaH)**(1/5)

Rey=(Q*4)/((math.pi)*D*v)

K=(0.25)/(math.log10(e/3.7*D)*((5.74)/Rey**0.9)**2


print('%.4f'%D)
print('%.4f'%Rey)
print('%.4f'%K)
