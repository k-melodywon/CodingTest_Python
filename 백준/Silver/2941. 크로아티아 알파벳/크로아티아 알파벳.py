import sys
a = sys.stdin.readline().strip()
b = 0
croatia =['c=', 'c-', 'dz=', 'd-','lj','nj','s=','z=']

for i in croatia:
    b += a.count(i)
    a = a.replace(i," ")
a = a.replace(" ","")
print(b+len(a))