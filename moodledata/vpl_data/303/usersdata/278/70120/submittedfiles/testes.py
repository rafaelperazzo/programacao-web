f = float(input('Digite f: '))
L = float(input('Digite L: '))
Q = float(input('Digite Q: '))
AH = float(input('Digite AH: '))
v = float(input('Digite v: '))
g = 9.81
e = 0.000002
pi = math.pi
D = ((8*f*L*Q*Q)/(pi*pi*g*AH))**0.2
print('%.4f' %(D))
Rey = 4Q/(pi*D*v)
print('%.4f' %(Rey))
k = 0.25/(math.log10(e/3.7*D + 5.74/(Rey)**0.9))**2
print('%.4f' %(k))
