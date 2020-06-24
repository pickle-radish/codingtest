import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())

for tc in range(1, N+1):
    P, Q, R, S, W = map(int, input().split())
    A_pay = P * W
    B_pay = Q if R > W else Q + (S *( W - R ))

    print(f'#{tc} {A_pay if A_pay < B_pay else B_pay}')