import sys

sys.setrecursionlimit(1000030)
input = sys.stdin.readline


def main():
    tc = int(input())
    for _ in range(tc):
        input()
        students = [int(_) - 1 for _ in input().split()]

        print(solve(students))


def solve(students):
    n_student = len(students)
    visited = [False for _ in range(n_student)]
    cnt = 0 # 그룹을

    for node in range(n_student):
        if not visited[node]:
            path = [node]
            dfs(students, visited, path, node)

            # ex,  path [4, 7, 6, 4]
            # ex2, path [1, 3, 3]
            start = next((i for i, x in enumerate(path)
                          if x == path[-1]
                          and i != len(path) - 1), None)

            if start is not None:
                cnt += len(path) - start - 1

    return n_student - cnt


def dfs(students, visited, path, node):
    visited[node] = True
    next_node = students[node]
    path.append(next_node)

    if not visited[next_node]:
        dfs(students, visited, path, next_node)


main()
