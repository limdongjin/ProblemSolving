

def solve(S):
    # sequences ret 
    lottos = []
    visited = [False]*len(S)
    
    go(0, 0, S, visited, lottos)
    print('\n'.join(lottos) + '\n')
    
def go(idx, start, S, visited, lottos):
    if idx == 6:
        lotto = ' '.join(map(str, [S[i] for i in range(len(S)) if visited[i]]))
        lottos.append(lotto)
        return
    
    for i in range(start, len(S)):
        if visited[i]:
            continue
        visited[i] = True
        go(idx+1, i+1, S, visited, lottos)
        visited[i] = False
    return

while True:
    input1 = list(map(int, input().split()))

    if len(input1) == 1:
        # end of program
        break

    N = input1[0]
    S = input1[1:][:]

    solve(S)
