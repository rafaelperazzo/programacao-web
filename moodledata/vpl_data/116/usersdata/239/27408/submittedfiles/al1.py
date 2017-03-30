# -*- coding: utf-8 -*-
#V=3,14159*R²*H
print("Calulando o volume de uma lata")#Enunciado
print("Obs1.: Utilize ponto (.) para separar casas decimais")#Observação técnica do aplicativo
print("")#Espaçamento
print("")
R = float(input("Digite o raio da lata: ")) #Declarando Raio
H = float(input("Digite a altura da lata: "))#Declarando Altura
V = 3.14159 * (R**2)*H #Fórmula para o volume
print("O volume da lata é: %.2f"%V) # Saída do valor