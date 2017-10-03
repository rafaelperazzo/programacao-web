# -*- coding: utf-8 -*-
import math
cv = int(input("Vitórias de C: "))
ce = int(input("Empates de C: "))
cs = int(input("Saldo de gols de C: "))
fv = int(input("Vitórias de F: "))
fe = int(input("Empates de C: "))
fs = int(input("Saldos de glos de F:"))
if ((cv*3)+ce)>((fv*3)+ce):
    print("C")
if ((cv*3)+ce)<((fv*3)+ce):
    print("F")
if ((cv*3)+ce)==((fv*3)+ce):
    if cs>fs