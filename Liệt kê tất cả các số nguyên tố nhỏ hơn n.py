def prime(a):
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            return False
    return True

def count(a):
    b=0
    for i in range(1,a):
        if prime(i):
            b+=1
    return b

while True:
    n=input('Input: ')
    if not n.isdigit():
        continue
    else:
        n=int(n)
        print(count(n))
    break