import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = input()

print(sum([int(i) for i in N]))
