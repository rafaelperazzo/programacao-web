"""
valor=["X","O"]
symh=valor[0]
sympc=valor[1]
print(symh)
print(sympc)
line1=[" "," "," "]
line2=[" "," "," "]
line3=[" "," "," "]   
print("|%s|%s|%s|" % (line1[0],line1[1],line1[2]) )
print("|%s|%s|%s|" % (line2[0],line2[1],line2[2]) )   
print("|%s|%s|%s|" % (line3[0],line3[1],line3[2]) )
line1[2]=symh
print("|%s|%s|%s|" % (line1[0],line1[1],line1[2]) )
print("|%s|%s|%s|" % (line2[0],line2[1],line2[2]) )   
print("|%s|%s|%s|" % (line3[0],line3[1],line3[2]) )
line2[1]=sympc
print("|%s|%s|%s|" % (line1[0],line1[1],line1[2]) )
print("|%s|%s|%s|" % (line2[0],line2[1],line2[2]) )   
print("|%s|%s|%s|" % (line3[0],line3[1],line3[2]) )
line3[2]=symh
print("|%s|%s|%s|" % (line1[0],line1[1],line1[2]) )
print("|%s|%s|%s|" % (line2[0],line2[1],line2[2]) )   
print("|%s|%s|%s|" % (line3[0],line3[1],line3[2]) )
"""
"""
x=int(input("Número de médias: "))
while x <= 1:
    x=int(input("Número de médias: "))
notas=[]
for i in range (0,x,1):
    notas.append(float(input("Insira a nota %d: " %(i+1))))
soma=sum(notas)
res=soma/x
print(res)
"""
# exercício 25
n=int(input("Insira n: "))
a=[]
b=[]
c=[]
cres1=0
cres2=0
cres3=0
decres1=0
decres2=0
decres3=0
consec1=0
consec2=0
consec3=0
for i in range (0,n,1):
    a.append(int(input("Digite o termo %d do vetor a: " %(i+1))))
for i in range (0,n,1):
    b.append(int(input("Digite o termo %d do vetor b: " %(i+1))))
for i in range (0,n,1):
    c.append(int(input("Digite o termo %d do vetor c: " %(i+1))))
for i in range (0,n-1,1):
    if a[i]<a[i+1]:
        cres1=cres1+1
for i in range (0,n-1,1):
    if b[i]<b[i+1]:
        cres2=cres2+1
for i in range (0,n-1,1):
    if c[i]<c[i+1]:
        cres3=cres3+1
for i in range (0,n-1,1):
    if a[i]>a[i+1]:
        decres1=decres1+1
for i in range (0,n-1,1):
    if b[i]>b[i+1]:
        decres2=decres2+1
for i in range (0,n-1,1):
    if c[i]>c[i+1]:
        decres3=decres3+1
for i in range (0,n-1,1):
    if a[i]==a[i+1]:
        consec1=consec1+1
for i in range (0,n-1,1):
    if b[i]==b[i+1]:
        consec2=consec2+1
for i in range (0,n-1,1):
    if c[i]==c[i+1]:
        consec3=consec3+1
if cres1==n-1:
    print("S")
else:
    print("N")
