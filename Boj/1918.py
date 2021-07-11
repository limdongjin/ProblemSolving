import sys
input = sys.stdin.readline

s = input().rstrip()
priority = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0,
    ')': 0
}
ret = ''
stack = []
for ch in s:
    if ch.isalpha():
        ret += ch
    elif priority[ch] >= 1:
        while stack and priority[stack[-1]] >= priority[ch]:
            ret += stack.pop()
        stack.append(ch)
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(':
            ret += stack.pop()
        stack.pop()

while stack:
    ret += stack.pop()

print(ret)