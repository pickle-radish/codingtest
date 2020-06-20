import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

TC = int(input())

for tc in range(1, TC+1):
    a, b = list(map(int, input().split()))
    
    sign = ''
    if a>b:
        sign='>'
    elif a<b:
        sign='<'
    else:
        sign='='
    print(f'#{tc} {sign}')
