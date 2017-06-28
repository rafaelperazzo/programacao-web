a=int(input('Digite a:'))
b=int(input('Digite b:'))
da=1
db=1
while a>=1:
    da=da+1
    a=a//10
while b>1:
    db=db+1
    b=b//10
print('quant de digitos de a: %d' %da)
print('quant de digitos de b: %d' %db)