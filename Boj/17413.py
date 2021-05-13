import sys
input = sys.stdin.readline

S = input().rstrip()
ret = '' 

tag_flag, stack = False, ''
for ch in S:
    if ch == '<': # 태그 시작
        ret += stack[::-1] + ch
        tag_flag, stack = True, ''
    elif ch == '>': # 태그 끝
        ret += ch
        tag_flag = False
    elif tag_flag: # 태그 내부
        ret += ch
    # 태그 외부
    elif ch == ' ':
        ret += stack[::-1] + ch
        stack = ''
    else:
        stack += ch

ret += stack[::-1]
print(ret)
