a = int(input('linhas'))
b = int(input('colunas'))
m = []
for i in range (0,a,1):
    l = []
    for j in range (0,b,1):
        val = int(input('digite valores'))
        l.append(val)
    m.append(l)
    
print (m)
