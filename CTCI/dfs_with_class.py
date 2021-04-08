class Node:
    def __init__(self, id):
        self.id = id
        self.adjs = []
        self.visited = False

    def set_edge(self, to_node):
        self.adjs.append(to_node)


def dfs(graph, node: Node, path):
    node.visited = True
    path.append(node)
    for next_node in node.adjs:
        if not next_node.visited:
            dfs(graph, next_node, path)

def dfs_stack_advanced(graph, node: Node, path):
    def visit(v: Node):
        v.visited = True
        path.append(v)
    stack = []
    stack.append(node)

    while stack:
        cur_node = stack[-1]
        stack.pop()

        if not cur_node.visited:
            visit(cur_node)

        # 역순으로 스택에 넣는 이유는 dfs 의 순서를 왼쪽->오른쪽 으로 유지하기위함이다.
        # 재귀로 dfs 로 구현했을때와 같은 경로를 얻기위함.
        for idx in range(len(cur_node.adjs)-1, -1, -1):
            if not cur_node.adjs[idx].visited:
                stack.append(cur_node.adjs[idx])

        # 아래 코드는 위와 같은 동작을 하면서 더 깔끔해보이지만,
        # 역순으로 만드는 비용이 발생하므로 비효율적이다.
        # for next_node in cur_node.adjs[::-1]:
        #     if not next_node.visited:
        #         stack.append(next_node)

def dfs_stack(graph, node: Node, path):
    def visit(v: Node):
        v.visited = True
        path.append(v)

    stack = []
    stack.append(node)

    visit(node)

    while stack:
        cur_node = stack[-1]

        for next_node in cur_node.adjs:
            if not next_node.visited:
                visit(next_node)
                stack.append(next_node)
                break

        if cur_node == stack[-1]:
            stack.pop()

graph = {}

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node0.set_edge(node1)
node1.set_edge(node2)
node2.set_edge(node0)
node2.set_edge(node3)
# 0 -> 1 -> 2 -> 0
#             -> 3

graph[node0.id] = node0
graph[node1.id] = node1
graph[node2.id] = node2
graph[node3.id] = node3

path = []
dfs_stack_advanced(graph, node1, path)
for node in path:
    print(node.id, end=' ')