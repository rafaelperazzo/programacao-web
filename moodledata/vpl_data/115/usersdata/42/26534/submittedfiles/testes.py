def polinomio(x): 
    f=(x**2)-2
    return f
a=int(input("digite o limite da esquerda: "))
b=int(input("digite o limite da direita: "))
c=(a+b)/float(2)
erro=b-a
print("passo,a,b,c,f(a),f(b),(fc),erro")
i=0

    print(i,a,b,c,polinomio(a),polinomio(b),polinomio(c),erro)
    if polinomio(c)<0:
        a=c
    if polinomio(c)>0:
        b=c
    erro=b-a
    i+=1
    

