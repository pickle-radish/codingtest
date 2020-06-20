import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())

for i in range(N):
    print(2**i, end=' ')
print(2**N)