import math

a = int(input("n1 ->"))
b = int(input("n2 ->"))
c = int(input("n3 ->"))

if a>b and a>c:
    if c>b:
        av = c
    else:
        av = b
if b>a and b>c:
    if a>c:
        av=a
    else:
        av = c
if c>a and c>b:
    if a>b:
        av=a
    else:
        av=b
print(av)




