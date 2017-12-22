n = int(input('tamanho de a:'))
m = int(input('tamanho de b:'))


l1 = []
l2 = []

for i in range (0,n,1):
    val1 = int(input('valores de a: '))
    l1.append(val1)
    
for i in range (0,m,1):
    val2 = int(input('valores de b: '))
    l2.append(val2)
    
l3 = []
for k in range (0,n,1):
for j in range (0,m,1):
if li[k]==l2[j]:
    l3.append(l1[k])
    
print (len(l3))

