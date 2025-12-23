a,b,c= map(int, input().split())
list = [a,b,c]
seen = set()
duplicates = []

if a == b or a == c or b == c:
    if a==b==c:
        print(10000+1000*a)
    else:
        for item in list:
            if item in seen and item not in duplicates:
                duplicates.append(item)
            seen.add(item)
        print(1000+100*duplicates[0])
else:
    print(100*max(list))