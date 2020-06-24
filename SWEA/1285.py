import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())

for tc in range(1, N+1):
    members = int(input())
    records = list(map(lambda x: abs(int(x)), input().split()))
    
    if members == len(records):
        print(f'#{tc} {min(records)} {records.count(min(records))}')