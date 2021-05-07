

def main():
    nums = []
    for _ in range(9):
        nums.append(int(input()))
    hsum = sum(nums)
    for i in range(0, 8):
        for j in range(i+1, 9):
            if hsum - nums[i] - nums[j] == 100:
                f, s = nums[i], nums[j]
                nums.remove(f)
                nums.remove(s)
                break
        if len(nums) == 7:
            break

    nums.sort()
    for num in nums:
        print(num)

main()
