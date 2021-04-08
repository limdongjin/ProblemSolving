
class Graph:
    class Node:
        def __init__(self, id):
            self.id = id
            self.adjs = []
            self.visited = False

    def __init__(self):
        self.nodes = {}

    def create_node(self, id):
        node = self.Node(id)
        self.nodes[id] = node

    def add_edge(self, from_id, to_id):
        from_node = self.nodes[from_id]
        to_node = self.nodes[to_id]

        from_node.adjs.append(to_node)

    def exist_path(self, from_id, to_id):
        self.dfs(from_id)
        ret = self.get_node(to_id).visited

        # visited 를 리셋
        for node in self.nodes.values():
            node.visited = False

        return ret

    def get_node(self, id):
        return self.nodes[id]

    def dfs(self, start_id):
        path = []
        def visit(node):
            node.visited = True
            path.append(node)

        stack = []
        stack.append(self.get_node(start_id))

        while stack:
            cur_node = stack[-1]
            stack.pop()

            if not cur_node.visited:
                visit(cur_node)

            for idx in range(len(cur_node.adjs) - 1, -1, -1):
                if not cur_node.adjs[idx].visited:
                    stack.append(cur_node.adjs[idx])
        return path

graph = Graph()
graph.create_node(1)
graph.create_node(2)
graph.create_node(3)
graph.create_node(4)

graph.add_edge(1, 2)
graph.add_edge(2, 4)
graph.add_edge(3, 1)

dfs_path = graph.dfs(1)
for p in dfs_path:
    print(p.id, end=' ')

assert graph.exist_path(3, 1)
assert graph.exist_path(1, 3) == False