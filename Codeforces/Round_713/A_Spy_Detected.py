import sys
input = sys.stdin.readline

def main():
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        nums = [int(_) for _ in input().split()]

        if nums[0] == nums[1]:
            for i in range(2, len(nums)):
                if nums[i] != nums[0]:
                    print(i + 1)
                    break
        else:
            for i in range(2, len(nums)):
                if nums[i] == nums[0]:
                    print(2)
                    break
                elif nums[i] == nums[1]:
                    print(1)
                    break
        # next test case

main()