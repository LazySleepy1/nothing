#Viết 1 chương trình nhận vào số có 2 chữ số
#nếu số đó là số nguyên tố và tổng 2 chữ số chia hết cho 2 thì kết thúc, còn không thì nhập lại đến chết
def prime(a):
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

def count(a):
    for i in range(1,a+1):
        if prime(i):
            e=[int(e) for e in str(i)]
            w=sum(e)
        else:
            return False
    return w

n=int(input('Input: '))
print(count(n))