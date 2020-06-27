import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

TC = int(input())

for tc in range(1, TC+1):
    days = int(input())
    prices = list(map(int, input().split()))
    income = 0
    while len(prices) != 0:
        maxPrice = max(prices)
        maxIndex = prices.index(maxPrice)
        for price in prices[:maxIndex]:
            income += maxPrice - price
        prices = prices[maxIndex+1:]
    print(f'#{tc} {income}')
