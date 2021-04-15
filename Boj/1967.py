import sys
sys.setrecursionlimit(200000000)

class Node:
    def __init__(self, id):
        self.id = id
        self.adjs = []
class Result:
    def __init__(self):
        self.u = -1
        self.pleng = -1

def main():
    n = int(input())
    nodes = [Node(i) for i in range(n)]
    visited1 = [False for _ in range(n)]
    for i in range(n-1):
        u, v, w = [int(_) for _ in input().split()]
        nodes[u-1].adjs.append((nodes[v-1], w))
        nodes[v-1].adjs.append((nodes[u-1], w))

    # Result 노드에는 최대 경로 길이를 저장한다.
    ret = Result()

    # 0 번째 노드에서 dfs 탐색을 하면서 최대 경로 길이을 ret 에 저장한다.
    dfs(node=nodes[0], visited=visited1, pleng=0, result=ret)

    ret2 = Result()
    visited2 = [False for _ in range(n)]
    dfs(node=nodes[ret.u], visited=visited2, pleng=0, result=ret2)

    print(ret2.pleng)


# pleng 에는 현재경로의 길이를 저장한다.
def dfs(node, visited, pleng, result):
    id = node.id
    visited[id] = True

    # 현재의 경로 길이가 지금까지의 최대 경로 길이보다 크기때문에, 최대 경로로 설정한다.
    if pleng > result.pleng:
        result.pleng = pleng
        result.u = id

    # 인접한 노드 중에 방문하지 않는 노드를 방문한다.
    for next_node, w in node.adjs:
        if not visited[next_node.id]:
            # 다음 방문한 노드의 가중치를 더해서 경로를 전달
            dfs(node=next_node, visited=visited, pleng=pleng + w, result=result)

main()