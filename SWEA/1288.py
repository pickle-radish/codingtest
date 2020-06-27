import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())

for tc in range(1, N+1):
    n = int(input())
    number = []
    count = 1
    while len(number) < 10:
        for i in str(n * count):
            if i not in number:
                number.append(i)
        count+=1
    print(f'#{tc} {n * (count-1)}')
