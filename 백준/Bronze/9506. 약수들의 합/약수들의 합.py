import sys
while True:
    a = int(sys.stdin.readline().strip())
    A_sum = 1
    A = [1]
    for i in range(2,a):
        if a % i == 0:
            A.append(i)
            A_sum += i

    if a == -1:
        break
    
    if A_sum == a:
        print(a, '=',' + '.join([str(i) for i in A]))
    else:
        print(a,'is NOT perfect.')