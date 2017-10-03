#EXERCICIO 1
n= int(input('Digite quantos lados deve ter o seu polígono: '))
nd= (n*(n-3))/2
print('%.1f' % nd)

#EXERCÍCIO 2
f= float(int('Digite um valor para f: '))
L= float(int('Digite um valor para L: '))
Q= float(int('Digite um valor para Q: '))
DeltaH= float(int('Digite um valor para DeltaH: '))
v= float(int('Digite um valor para v: '))
g= 9.81
libra= 0.000002
pi= (math.pi)

D= (((8*f*L*(Q**2))/((pi**2)*g*DeltaH))**(1/5)
Rey= (4*Q)/(pi*D*v)
k= (0.25)/((match.log10(((libra)/(3*D))+((5.74)/(Rey**0.9)))**2)

print('%.4f' % D)
print('%.4f' % Rey)
print('%.4f' % k)