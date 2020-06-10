## JadenCase문자열 만들기 - 12951

https://programmers.co.kr/learn/courses/30/lessons/12951



source code

```python
def solution(s):
    answer = ''
    s = s.lower()    
    for word in s.split(" "):
        word= word.capitalize()
        answer+=word+' '
    return answer[:-1]
```

