import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

N = int(input())

for tc in range(1, N+1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    thirty = [4, 6, 9, 11]
    result = True

    if int(month) > 12 or int(month)==0:
        result = False
    else:
        if int(month)==2:
            if int(day) > 28:
                result = False
        elif int(month) in thirty:
            if int(day) > 30:
                result = False
        else:
            if int(day) > 31:
                result = False
    if result:
        print(f'#{tc} {year}/{month}/{day}')
    else:  
        print(f'#{tc} -1')