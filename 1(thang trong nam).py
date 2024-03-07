#Bài 1: Nhập vào tháng của 1 năm. Cho biết tháng thuộc quý mấy trong năm
def month(month):
    if month >= 1 and month <= 3:
        quarter = 1
    elif month >= 4 and month <= 6:
        quarter = 2
    elif month >= 7 and month <= 9:
        quarter = 3
    elif month >= 10 and month <= 12:
        quarter = 4
    else:
        return False
    return quarter
while True:
    n=input('Input: ')
    if not n.isdigit():
        continue
    else:
        print(month(n))
    break