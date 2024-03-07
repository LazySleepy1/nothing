#Viết 1 chương trình nhận vào số có 2 chữ số, nếu số đó là số nguyên tố và tổng 2 chữ số chia hết cho 2 thì kết thúc, còn không thì nhập lại đến chết
def prime(a):
    if a<=10:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

def tong(a):
    if prime(a):
        b=[int(b) for b in str(a)]
        c=sum(b)
    else:
        return False
    return c

while True:
    n=input('Input: ')
    if not n.isdigit():
        continue
    else:
        n=int(n)
        print(tong(n))
    break