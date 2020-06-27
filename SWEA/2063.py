import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr[N//2])