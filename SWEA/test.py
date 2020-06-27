# test 2046이라고 입력 받았을 때,

# 2046.py 실행 결과와 output_2046.txt 의 결과가 같을 때
# => '맞았습니다' 출력 
# 아니면 '틀렸습니다' 출력

import os
import sys

sys.stdout = open('testOutput.txt', 'w')


os.system('python 2063.py')

print('a')
