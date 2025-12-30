import sys
word = sys.stdin.readline().strip()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in word:
        print(word.find(i))
    else:
        print('-1')
