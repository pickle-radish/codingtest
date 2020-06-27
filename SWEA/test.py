# test 2063이라고 입력 받았을 때,

# 2063.py 실행 결과와 output_2063.txt 의 결과가 같을 때
# => '맞았습니다' 출력 
# 아니면 '틀렸습니다' 출력
import os
import sys

if len(sys.argv) == 1:
    print('문제 번호를 입력하세요')
    sys.exit(1)

problem_number = sys.argv[-1]

os.system(f'python {problem_number}.py > testOutput.txt')
result = os.system(f'cmp testOutput.txt output_{problem_number}.txt')


if not result:
    print('맞았습니다')
else:
    print('틀렸습니다')

os.system('rm -f testOutput.txt')