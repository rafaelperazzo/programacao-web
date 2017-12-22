def converterDecimal(valor):
    resultado = 0
    expoente = 0
    for i in valor[::-1]:
        resultado += int(i)**(len(valor)-expoente)
        print(resultado)
        expoente += 1 
    return resultado

print(converterDecimal('1011'))

