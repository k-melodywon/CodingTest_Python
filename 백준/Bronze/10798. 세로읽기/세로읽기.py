import sys

A = []
for _ in range(5):
    A.append(sys.stdin.readline().rstrip())

word = ''
max_len = max(len(s) for s in A)

for i in range(max_len):
    for j in range(5):
        if i < len(A[j]):
            word += A[j][i]

print(word)