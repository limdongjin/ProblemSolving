from collections import deque

MAX = 100001


def solve(n: int, k: int):
    cache = [0] * MAX
    queue = deque()
    queue.append(n)

    while queue:
        nn = queue.popleft()
        if nn == k:
            break
        for _ in (nn - 1, nn + 1, nn * 2):
            if _ < 0 or _ >= MAX or cache[_]:
                continue
            cache[_] = cache[nn] + 1
            queue.append(_)

    return ans


n, k = (int(x) for x in input().split())
print(solve(n, k))
