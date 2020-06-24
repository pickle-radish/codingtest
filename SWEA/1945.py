import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())

for tc in range(1, N+1):
    num = int(input())
    div = [2,3,5,7,11]
    answer=[0,0,0,0,0]
    for i, n in enumerate(div):
        while num%n==0:
            answer[i] += 1
            num = num / n
    print(f"#{tc} {' '.join(map(str, answer))}")