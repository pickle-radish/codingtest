import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

P, K = map(int, input().split())
print(P-K + 1)