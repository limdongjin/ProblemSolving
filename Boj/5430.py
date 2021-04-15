import sys


input = sys.stdin.readline
def main():
    tc = int(input())
    for _ in range(tc):
        op = input()
        n = int(input())
        if n == 0:
            input()
            if 'D' in op:
                print('error')
            else:
                print('[]')
            continue

        nums = [int(num)
                for num in input()
                    .replace('[', '')
                    .replace(']', '')
                    .split(',')]

        left = 0
        right = n - 1
        is_left = True
        is_empty = False
        is_error = False
        for c in op:
            if c == 'R':
                is_left = not is_left
            elif c == 'D':
                if is_empty:
                    is_error = True
                    break
                elif is_left:
                    left = left + 1
                elif not is_left:
                    right = right - 1

                if left > right:
                    is_empty = True
        if is_error:
            print('error')
        else:
            if is_left:
                ret = [str(_) for _ in nums[left:right+1]]
            else:
                ret = [str(_) for _ in nums[left:right+1]]
                ret.reverse()
            print('[' + ",".join(ret)+']')

main()
