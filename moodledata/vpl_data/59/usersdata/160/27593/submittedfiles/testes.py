a=input('digite a:')
b=input('digite b:')
c=input('digite c:')

Delta=a*(x*x)+b*x+c

x1=(-b+((Delta)**(1/2)))/2*a
x2=(-b-((Delta)**(1/2)))/2*a


if Delta>0: print(x1) print(x2)
elif Delta=0: print (x1) print(x2)
else: print ("SRR")

