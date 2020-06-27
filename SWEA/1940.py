import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

TC = int(input())

for tc in range(1, TC+1):
    count = int(input())
    speed = 0
    distance = 0
    for i in range(count):
        command = list(map(int, input().split()))

        if command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            if speed < command[1]:
                speed = 0
            else:
                speed -= command[1]
        
        distance += speed
   
    print(f'#{tc} {distance}')

    