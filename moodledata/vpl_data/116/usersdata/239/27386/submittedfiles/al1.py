# -*- coding: utf-8 -*-
#V=3,14159*R²*H
print("Calulando o volume de uma lata")
print("Obs1.: Utilize ponto para separar casas decimais")
R = float(input("Digite o raio da lata: "))
H = float(input("Digite a altura da lata: "))
V = 3.14159 * (R**2)*H
print("O volume da lata é: %.2f"%V)