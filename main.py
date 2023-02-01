import math
def total_price(price,vat):
    new_price = price + math.ceil((vat/100)*price)
    return new_price
x = int(input())
y = int(input())
print(total_price(x,y))
