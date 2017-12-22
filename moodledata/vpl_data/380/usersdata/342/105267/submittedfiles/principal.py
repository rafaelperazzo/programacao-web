
a = int(input('quant de colunas'))
b = int(input('quant de linhas'))
q = int(input('quant de colunas'))
c = 0
i = 2

while i<=q:
    if a%i==0 and b%i==0:
        c = c+1
    i = i +1
print (c)
    
    

    
