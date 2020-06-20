import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())

for tc in range(1, N+1):
    arr = map(int, input().split())
    print(f'#{tc} {sum([i for i in arr if i%2])}')