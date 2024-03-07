def iuiem(a):
    b=0
    for i in range(1,a+1):
        b=+i
    return b

while True:
    a = input("Input Number: ")
    if not a.isdigit():
        continue
    else:
        a=int(a)
        print(iuiem(a))
    break