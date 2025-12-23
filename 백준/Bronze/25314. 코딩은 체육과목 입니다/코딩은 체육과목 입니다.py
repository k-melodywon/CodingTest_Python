num= int(input())
name = ''

if num%4 != 0:
   num = num//4 + 1
else:
   num = num//4
   
for i in range(0,num):
   name += 'long '
name += 'int'
print(name)