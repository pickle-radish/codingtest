import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())
arr = sorted(list(range(1, N+1)), reverse=True)
for i in arr:
    print(i , end=' ')
print('0')