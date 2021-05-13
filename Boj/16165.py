from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
team_mem, mem_team = {}, {}

for i in range(N):
    tname, n_mem  = input().rstrip(), int(input())
    team_mem[tname] = []    
    for j in range(n_mem):
        name = input().rstrip()
        team_mem[tname].append(name)
        mem_team[name] = tname
for team in team_mem:
    team_mem[team] = '\n'.join(sorted(team_mem[team]))

buf = ''
for i in range(M):
    name, typ = input().rstrip(), input().rstrip()
    buf += team_mem[name] if typ == '0' else mem_team[name]
    buf += '\n'

print(buf, end='')
