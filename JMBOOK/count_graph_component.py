
# 그래프가 주어졌을때, 한 노드에서 다른 노드까지 가는 경로가 있다면,
# 두 노드는 같은 그룹이라 하자.
# 그룹의 수를 구해라.
class Node:
    def __init__(self, data):
        self.data = data
        self.childs = []
        self.visited = False


class Graph:
    def __init__(self):
        self.nodes = {}
    def add_node(self, data):
        node = Node(data)
        self.nodes[data] = node
    def add_edge(self, from_id, to_id):
        from_node = self.nodes[from_id]
        to_node = self.nodes[to_id]
        from_node.childs.append(to_node)
    def get_group_cnt(self):
        cnt = 0
        for node in self.nodes.values():
            if not node.visited:
                cnt += 1
                self.dfs(node)
        return cnt
    def dfs(self, node):
        node.visited = True
        for adj in node.childs:
            if not adj.visited:
                self.dfs(adj)


def main():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')

    graph.add_node('d')
    graph.add_node('e')

    graph.add_edge('a', 'b')
    graph.add_edge('b', 'c')

    cnt = graph.get_group_cnt()
    print(cnt)

main()