import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())

for i in range(1, N//2+1):
    if not N%i :
        print(i, end=' ')
print(N)