a= int(input('Digite seu investimento:'))
t= int(input('Digite sua taxa de lucro:'))
for i in range (a,11,t):
    a=a+(a*t)
    print (i)
    