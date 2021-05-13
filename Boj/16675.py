

a1, a2, b1, b2 = ('SPR'.index(v) for v in input().split())

if a1 == a2 and (a1+2)%3 in (b1, b2):
    print('TK')
elif b1 == b2 and (b1+2)%3 in (a1, a2):
    print('MS')
else:
    print('?')
