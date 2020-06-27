import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

number = int(input())

for n in range(1, number+1):
    clapNumber = [3,6,9]
    clap = False
    clapCount = 0
    for i in str(n): 
        if int(i) in clapNumber:
            clapCount+=1
            clap=True

    if clap:
        print("-" * clapCount, end=" ")
    else:
        print(n, end=" ")