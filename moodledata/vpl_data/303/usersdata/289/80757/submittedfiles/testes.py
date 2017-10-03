A = int(input("Digite o primeiro lado: "))
B = int(input("Digite o segundo lado: "))
C = int(input("Digite o terceiro lado: "))
if A<B+C and B<A+C and C<A+B:
    print("Podem formar um triângulo")
else:
    print("Não pode ")
