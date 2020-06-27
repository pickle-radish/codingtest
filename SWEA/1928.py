import sys
sys.stdin = open('input_' + sys.argv[0][:-3] + '.txt')

TC = int(input())

for tc in range(1, TC+1):
    baseCode = input()
    answer = ''
    while baseCode:
        binaryCode = ''
        for i in baseCode[:4]:
            if i.islower():
                binaryCode += bin(ord(i) - 71)[2:].zfill(6)
            elif i.isupper():
                binaryCode += bin(ord(i) - 65)[2:].zfill(6)
            elif i.isdigit():
                binaryCode += bin(ord(i) + 4)[2:].zfill(6)
            elif i == '+':
                binaryCode += bin(62)[2:].zfill(6)
            else:
                binaryCode += bin(63)[2:].zfill(6)

        for i in range(3):
            answer += chr(int(binaryCode[:8], 2))
            binaryCode = binaryCode[8:]
        baseCode = baseCode[4:]
    
    print(f'#{tc} {answer}')