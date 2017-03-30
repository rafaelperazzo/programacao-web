def polinomio(x): 
    f=x**2-2
    return f
a=input("digite o limite da esquerda: ")
b=input("digite o limite da direita: ")
c=(a+b)/2.0
erro=b-a
print("passo,a,b,c,f(a),f(b),(fc),erro")
i=0
while erro>0.01:
    v=[(i)]

