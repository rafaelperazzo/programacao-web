
a = float(input('informe o numero a: ' ))
b = float(input('informe o numero b: ' ))
c = float(input('informe o numero c: ' ))
d = float(input('informe o numero d: ' ))

 
x = -100.0
soma = 0 
    
while True:
    h = (a*x**3) + (b*x**2) + (c*x) + d
    soma = soma + 0.1
    x = x + soma 
    if h == 0:
        break
print('%.1f' %x)
     

    

    































