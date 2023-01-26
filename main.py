import math
def total_price(price,vat):
    new_price = price + math.ceil((vat/100)*price)
    return new_price
num = list(map(int,input().split()))
print(total_price(num[0],num[1]))
