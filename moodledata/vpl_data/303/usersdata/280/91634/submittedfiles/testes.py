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