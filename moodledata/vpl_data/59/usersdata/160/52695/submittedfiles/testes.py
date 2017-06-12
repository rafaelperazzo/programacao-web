
def numerofeliz(n):
    x=1
    while n!=1:
        a=0
        s=str(n)
        for i in range(len(s)):
            a=a+int(s[i]**2)
        n=a
        if n==1:
            return(True)
        x+=1
        if x==20:
            return(False)
for i in range(1,501):
    if i==1:
        print(i)
    if numerofeliz(i):
        print(i)