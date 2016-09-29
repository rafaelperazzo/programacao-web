# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv = input("Digite o número de Cv:")
Ce = input("Digite o número de Ce:")
Cs = input("Digite o número de Cs:")
Fv = input("Digite o número de Fv:")
Fe = input("Digite o número de Fe:")
Fs = input("Digite o número de Fs:")

if Cv+Ce>Fv+Fe:
    print("C")
else:
    print("F")
if Cv+Ce==Fv+Fe and Cs>Fs:
    print("C")
if Cv+Ce==Fv+Fe and Cs<Fs:
    print("F")
if Cv+Ce==Fv+Fe and Cs==Fs:
    print("=")
