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
    cache = [-1 for i in range(n)]
    for i in range(n-1):
        u, v, w = [int(_) for _ in input().split()]
        nodes[u-1].adjs.append((nodes[v-1], w))
        nodes[v-1].adjs.append((nodes[u-1], w))

    ret = Result()
    dfs(node=nodes[0], cache=cache, pleng=0, result=ret)

    ret2 = Result()
    cache2 = [-1 for i in range(n)]
    dfs(node=nodes[ret.u], cache=cache2, pleng=0, result=ret2)
    print(ret2.pleng)


def dfs(node, cache, pleng, result):
    id = node.id
    cache[id] = pleng

    if cache[id] > result.pleng:
        result.pleng = cache[id]
        result.u = id

    for next_node, w in node.adjs:
        if cache[next_node.id] == -1:
            dfs(node=next_node, cache=cache, pleng=pleng + w, result=result)

main()