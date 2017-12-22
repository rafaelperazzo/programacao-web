def converterDecimal(valor):
    resultado = 0
    expoente = 0
    for i in valor[::-1]:
        print(i)
        resultado += int(i)**(len(valor)-expoente)
        print(resultado)
        expoente = expoente + 1 
    return resultado

print(converterDecimal('1011'))

