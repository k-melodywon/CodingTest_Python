
sum= int(input())
product_num= int(input())

for i in range(0,product_num):
    price, amount = map(int, input().split())
    sum -= price*amount
if sum == 0 :
    print('Yes')
else:
    print('No')