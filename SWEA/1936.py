import sys
sys.stdin = open('input_1936.txt')

A, B = list(map(int, input().split()))

if A%3 > B%3:
    print('A')
else:
    print('B')