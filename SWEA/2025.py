import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())

print(sum(range(N+1)))