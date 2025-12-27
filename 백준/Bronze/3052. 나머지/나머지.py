
import sys
basket = []

for i in range(10):
    a = int(sys.stdin.readline().strip())
    if (a%42) not in basket :
        basket.append(a%42)

 

print(len(basket))