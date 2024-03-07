def tich(a):
    b=[int(b) for b in a]
    c=1
    for i in b:
        c*=i
    return c
while True:
    n=input('Input: ')
    if not n.isdigit(): 
        continue
    else:
        print(tich(n))
    break