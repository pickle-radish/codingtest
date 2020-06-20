import sys
sys.stdin = open('1938_input.txt', )

a, b = list(map(int, input().split(' ')))

print(a+b)
print(a-b)
print(a*b)
print(a//b)