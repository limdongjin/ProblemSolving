import sys
input = sys.stdin.readline

def solve():
    # global : visited, ret
    for start_city in range(n):
        visited[start_city] = True
        go(path=[start_city],
                cost=0,
                visit_cnt=1)
        visited[start_city] = False
    
    print(ret)

# dfs+backtracking travasal function
def go(path, cost, visit_cnt):
    global ret
    # global : ret, costs, visited

    if cost >= ret:
        return

    last = path[-1]
    if visit_cnt == len(costs):
        # travasal finish

        start = path[0]
        if costs[last][start] != 0:
            ret = min(ret, cost+costs[last][start])
        return

    for i in range(n):
        if visited[i] or costs[last][i] == 0:
            continue
        visited[i] = True
        path.append(i)

        go(path,cost+costs[last][i],visit_cnt+1)
        
        visited[i] = False
        path.pop()
    return

n = int(input())
costs = [[int(_) for _ in input().split()] 
                   for y in range(n)]
visited = {city: False for city in range(n)}
ret = sys.maxsize

solve()
