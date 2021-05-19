

def solve(s):
    stack = []
    
    for br in s:
        if br in pair_br:
            stack.append(br)
            continue
        if not stack or pair_br[stack.pop()] != br:
            return False

    if stack:
        return False

    return True
pair_br = {'(': ')', '{': '}', '[': ']'}
for _ in range(int(input())):
    S = input().rstrip()
    
    if solve(S):
        print('YES')
    else:
        print('NO')
