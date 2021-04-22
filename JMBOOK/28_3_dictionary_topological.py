import sys
input = sys.stdin.readline

def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        words = []
        for i in range(n):
            words.append(input())

        ret =solve(words)
        if len(ret) == 0:
            print("impossible!")
        else:
            for _ in ret:
                print(_, end=' ')


def solve(words):
    n = len(words)
    graph = [[0 for i in range(26)] for j in range(26)]

    # 글자->글자 모양의 그래프 관계를 생성한다.
    for right in range(1, n):
        left = right - 1
        len_common = min(len(words[left]), len(words[right]))
        for i in range(0, len_common):
            ch1 = words[left][i]
            ch2 = words[right][i]
            if ch1 != ch2:
                graph[ord(ch1) - ord('a')][ord(ch2) - ord('a')] = 1
                break

    visited = [False for _ in range(26)]
    orders = []
    # dfs 를 수행하고, 위상 정렬 결과를 orders 에 저장한다.
    for i in range(26):
        if not visited[i]:
            dfs(graph, i, orders, visited)
    orders.reverse()

    for left in range(26):
        for right in range(left+1, 26):
            if graph[orders[right]][orders[left]] == 1:
                return []
    orders = [chr(_ + ord('a')) for _ in orders]
    return orders


def dfs(graph, node, orders, visited):
    visited[node] = True
    m = len(graph)
    for next_node in range(m):
        if graph[node][next_node] == 1 and not visited[next_node]:
            dfs(graph, next_node, orders, visited)
    orders.append(node)


main()