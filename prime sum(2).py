#Nhập vào 1 khoảng Start và End, Đếm số lượng và tính tổng các số nguyên tố có trong khoản
def prime(a):
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

def count(a,b):
    c=0
    d=0
    for i in range(a,b+1):
        if prime(i):
            c+=1
            d+=i
    return c,d

start=int(input('Start: '))
end =int(input('End:'))

c=count(start,end)
print(c)