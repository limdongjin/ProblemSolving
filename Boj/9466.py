import sys

sys.setrecursionlimit(1000030)
input = sys.stdin.readline


def main():
    tc = int(input())
    for _ in range(tc):
        input()
        students = [int(_) - 1 for _ in input().split()]

        print(solve_upgrade(students))
        # print(solve(students))

# 위상 정렬 아이디어와 유사한듯하다.
# indegree 가 0 이면 사이클에 속할수 없음을 이용한 풀이
# 또한 indegree 가 0 인 노드를 그래프에서 제거(가리키는 노드의 indegree 감소) 했을때도
# 다시 위의 규칙이 적용됨을 이용한것.
# 2800ms
def solve_upgrade(students):
    indegree = [0 for _ in range(len(students))]
    visited = [False for _ in range(len(students))]

    for st in students:
        indegree[st] += 1

    cnt = 0
    for i in range(len(students)):
        cur = i
        while indegree[cur] == 0 and not visited[cur]:
            visited[cur] = True
            indeg66ree[students[cur]] -= 1
            cur = students[cur]
            cnt += 1

    return cnt

# 오일러 서킷에서 아이디어 얻음.
# dfs 를 돌려서 나온 경로에서 사이클을 찾는 방법
# 만일 사이클이 있다면 dfs 가 마지막으로 방문한 노드는 반드시 사이클의 시작점이자 끝점일수밖에 없음
# 5400ms
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
