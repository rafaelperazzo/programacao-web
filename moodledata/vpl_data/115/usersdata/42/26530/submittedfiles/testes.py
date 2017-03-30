def polinomio(x): 
    f=x**2-2
    return f
a =int( input("digite o limite da esquerda: "))
b = int(input("digite o limite da direita: "))
print a
print b
c=(a+b)/float(2)
erro=b-a
print("passo,a,b,c,f(a),f(b),(fc),erro")
i=0
while erro>0.01:
    v=[(i)]

