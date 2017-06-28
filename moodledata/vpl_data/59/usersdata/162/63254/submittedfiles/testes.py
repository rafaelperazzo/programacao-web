a=int(input('Digite a:'))
b=int(input('Digite b:'))
da=0
db=0
while a>=0:
    da=da+1
    a=a//10
while b>0:
    db=db+1
    b=b//10
print('quant de digitos de a: %d' %da)
print('quant de digitos de b: %d' %db)