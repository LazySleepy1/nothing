def fibonaci(a):
    if a==1:
        return [0]
    elif a==2:
        return [1]
    else:
        b=[0,1]
        while len(b)<int(a):
            b.append(b[-1]+b[-2])
    return b
while True:
    n=input('Input: ')
    if not n.isdigit():
        continue
    else:
        n=int(n)
        print(fibonaci(n)[n-1])
    break