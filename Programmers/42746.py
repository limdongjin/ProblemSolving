# #
# # https://programmers.co.kr/learn/courses/30/lessons/42746
# # 가장 큰 수
# #
#
#
# def solution(numbers):
#     nums = sorted(map(str, numbers), reverse=True)
#     i = 0
#     nums_len = len(nums)
#     while i < nums_len - 1:
#         j = 0
#         while j < nums_len - 1:
#             print(nums[j] + nums[j+1], nums[j]+nums[j+1])
#             if int(nums[j] + nums[j+1]) < int(nums[j+1] + nums[j]):
#                 tmp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = tmp
#             j += 1
#         i += 1
#     print(nums)
#     return "".join(nums)
#
#
# def test_solution():
#     # assert solution([6, 10, 2]) == "6210"
#     assert solution([3, 30, 34, 5, 9]) == "9534330"
#
#
# test_solution()