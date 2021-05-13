import sys
input=sys.stdin.readline
_, A, _ = input(), input().split(), input()
is_exist = {v: '1' for v in A}

print('\n'.join([is_exist.get(v, '0') for v in input().split()]))
