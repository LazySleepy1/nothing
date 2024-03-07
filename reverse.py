def prime(a):
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

def count(a,b):
    if a<1 or b<1:
        return False
    elif a>=1 and b<=10:
        return [2,3,5,7]
    else:
        q=[]
        for i in range(int(a),int(b)+1):
            if prime(i):
                q.append(prime(int(str(i)[::-1])))
    return q
while True:
    a=input('Start: ')
    b=input('End: ')
    if not a.isdigit() and not b.isdigit():
        continue
    else:
        a=int(a)
        b=int(b)
        print(count(a,b))
    break