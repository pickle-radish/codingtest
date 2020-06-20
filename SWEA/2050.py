import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = input()

for i in range(len(N)-1):
    print(ord(N[i])-64, end=' ')
print(ord(N[-1])-64)