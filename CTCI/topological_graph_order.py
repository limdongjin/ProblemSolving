# 4.7 순서 정하기

def main():
    # f -> c -> a -> e
    #   -> b -> a -> e
    # d -> e
    graph = build_given_graph()
    orders = find_build_order(graph)
    print([order.data for order in orders])

def find_build_order(graph):
    orders = []
    cur = 0
    orders.extend(graph.get_inorder_zero_nodes())

    while cur < len(orders):
        node = orders[cur]

        for adj_node in node.childs:
            adj_node.indegree -= 1
            if adj_node.indegree == 0:
                orders.append(adj_node)
        cur = cur + 1
    if len(graph.nodes) != cur:
        raise Exception('수행 할수없는 경우입니다')
    return orders


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = []
    def add_node(self, data):
        self.nodes[data] = Node(data)

    def add_edge(self, from_id, to_id):
        from_node = self.nodes[from_id]
        to_node = self.nodes[to_id]
        from_node.childs.append(to_node)

        from_node.outdegree += 1
        to_node.indegree += 1

    def get_inorder_zero_nodes(self):
        return [node for node in self.nodes.values() if node.indegree == 0]
class Node:
    def __init__(self, data):
        self.data = data
        self.childs = []
        self.indegree = 0
        self.outdegree = 0

def build_given_graph():
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('e')
    graph.add_node('f')
    graph.add_node('e')
    graph.add_node('g')

    # graph.add_edge('b', 'f') # 사이클을 만들면 예외가 반환된다.
    graph.add_edge('f', 'b')
    graph.add_edge('f', 'c')
    graph.add_edge('f', 'a')

    graph.add_edge('d', 'g')
    graph.add_edge('c', 'a')
    graph.add_edge('b', 'a')

    graph.add_edge('a', 'e')
    return graph

main()
