import sys
input=sys.stdin.readline

def inorder(node, g):
    if not g[node]:
        return ''
    left, right = g[node][0], g[node][1]
    ret = inorder(left, g) + node + inorder(right, g)
    return ret

def preorder(node, g):
    if not g[node]:
        return ''
    left, right = g[node][0], g[node][1]
    ret = node + preorder(left, g) + preorder(right, g)
    return ret

def postorder(node, g):
    if not g[node]:
        return ''
    left, right = g[node][0], g[node][1]
    ret = postorder(left, g) + postorder(right, g) + node
    return ret

N = int(input())
graph = {'.': None}

for _ in range(N):
    p, l, r = input().split()
    graph[p] = [l, r]

print(preorder('A', graph))
print(inorder('A', graph))
print(postorder('A', graph))

