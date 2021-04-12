import heapq
import sys

# 이 입력 함수를 사용해야 AC 를 받을수있음
input = sys.stdin.readline

def main():
    n = int(input())
    h = []
    for i in range(n):
        num = int(input())
        if num != 0:
            heapq.heappush(h, (abs(num), num))
        elif num == 0:
            if not h:
                print(0)
                continue
            _, val = heapq.heappop(h)
            print(val)
main()