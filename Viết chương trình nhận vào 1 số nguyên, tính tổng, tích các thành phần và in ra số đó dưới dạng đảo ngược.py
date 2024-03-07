#Viết chương trình nhận vào 1 số nguyên, tính tổng, tích các thành phần và in ra số đó dưới dạng đảo ngược
def tongtich(a):
    c=1
    d=[int(f) for f in str(a)]
    b=sum(d)
    w=int(str(b)[::-1])
    for i in d:
        c*=i
    e=int(str(c)[::-1])
    return e,w
n=int(input('Input: '))
print(tongtich(n))