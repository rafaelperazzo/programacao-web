a=int(input('Digite a:'))
b=int(input('Digite b:'))
e=0
for i in range(1,a+1,1):
    c=int(input('Digite c:'))
    d=int(input('Digite d:'))
    if c+d>=b:
        e=e+1
    if i==a:
        print(e)
  
    