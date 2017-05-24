n=int(input('digite um ano:'))
if (n%400==0) or (n%4==0 and n%100!=0):
    print('bissexto')
else:
    print('não')
