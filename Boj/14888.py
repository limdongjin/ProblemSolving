from enum import Enum
import sys

# using backtracking
class Solution:
    def __init__(self):
        self.max = -sys.maxsize
        self.min = sys.maxsize
    def main(self):
        self.N = int(input())
        self.A = list(map(int, input().split()))
        tmp = list(map(int, input().split()))
        self.op = ['+']*tmp[0] + ['-']*tmp[1] + ['X']*tmp[2] + ['/']*tmp[3]
        self.visited = [False for i in range(self.N-1)]
        self.go(0, self.A[0])
        print(self.max)
        print(self.min)
        
    def go(self, idx, cur_sum):
        if idx >= self.N - 1:
            self.max = max(cur_sum, self.max)
            self.min = min(cur_sum, self.min)
            return
        target = self.A[idx+1]
        next_sum = {'+': cur_sum + target, 
                  '-': cur_sum - target, 
                  'X': cur_sum * target, 
                  '/': cur_sum // target if cur_sum >= 0 
                                    else -1*(abs(cur_sum)//target)}
        for op_i, op_v in enumerate(self.op):
            if self.visited[op_i]:
                continue
                
            self.visited[op_i] = True
            self.go(idx+1, next_sum[op_v])
            self.visited[op_i] = False

# using permutation
class Solution2:
    def __init__(self):
        self.max = -sys.maxsize
        self.min = sys.maxsize
        self.N = int(input())
        self.A = list(map(int, input().split()))
        tmp = list(map(int, input().split()))
        self.op = [0]*tmp[0] + [1]*tmp[1] + [2]*tmp[2] + [3]*tmp[3]
    def main(self):
        self.calc_all()
        while self.next_perm():
            self.calc_all()
        print(self.max)
        print(self.min)
    def calc_all(self):
        ret = self.A[0]
        for op_i, op_v in enumerate(self.op):
            ret = self.calc(ret, self.A[op_i + 1], op_v)
        self.max = max(self.max, ret)
        self.min = min(self.min, ret)
    def calc(self, a, b, op_v):
        if op_v == 0:
            return a + b
        elif op_v == 1:
            return a - b
        elif op_v == 2:
            return a * b
        elif op_v == 3:
            if a < 0:
                return (-1)*(abs(a)//b)
            else:
                return a // b
    def next_perm(self):
        # find i
        i = self.N - 2
        while i > 0 and self.op[i-1] >= self.op[i]:
            i -= 1
        if i <= 0:
            return False
        # find j
        j = self.N - 2
        while j > 0 and self.op[j] <= self.op[i-1]:
            j -= 1
        # swap
        self.op[i-1], self.op[j] = self.op[j], self.op[i-1]
        # reverse
        k = self.N - 2
        while i < k:
            self.op[i], self.op[k] = self.op[k], self.op[i]
            i += 1
            k -= 1
        return True

Solution2().main()
