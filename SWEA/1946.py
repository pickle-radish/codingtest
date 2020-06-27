import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

TC = int(input())

for tc in range(1, TC+1):
    print(f'#{tc}')
    inputCount = int(input())
    contents = []


    for i in range(inputCount):
        contents.append(input().split())

    curWidth = 1
    for content in contents:
        for i in range(int(content[1])):
            if curWidth < 10:
                print(content[0], end='')
                curWidth += 1
            else:
                print(content[0])
                curWidth = 1
    print()