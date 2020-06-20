import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())

for tc in range(1, N+1):
    arr = list(map(int, input().split()))
    print(f'#{tc} {round(sum(arr)/len(arr))}')