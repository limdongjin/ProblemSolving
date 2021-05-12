import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    nums = [int(_) for _ in input().split()]
    
    nums.sort()
    if nums[1] != nums[2]:
        print("NO")
    else:
        print("YES")
        print(nums[2], nums[0], nums[0])
