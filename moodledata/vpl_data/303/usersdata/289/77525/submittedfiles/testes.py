n = int(input("Digite sua idade:"))

if 0<n<=12:
    print("criança")
if 12<n<=16:
    print("adolescente")
if 16<n<=60:
    print("adulto")
if n>60:
    print("idoso")