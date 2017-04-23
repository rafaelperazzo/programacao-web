P=int(input('Digite a posição P:'))
R=int(input('Digite a posição R:'))
if P==0 and (R==0 or R==1):
    print(C)
elif P==1 and R==1:
    print(B)
else:
    print(A)
