# #
# # https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
# # 더 맵게
# #
#
#
# class BinHeap:
#     def __init__(self):
#         self.data = []
#         self.length = 0
#         self.real_length = 0
#
#     def insert(self, value):
#         if self.real_length != 0 and len(self.data) > self.length:
#             self.data[self.length] = value
#         else:
#             self.data.append(value)
#             self.real_length += 1
#         self.length += 1
#         idx = self.length - 1
#         while idx > 0:
#             p = (idx) // 2
#             if self.data[idx] < self.data[p]:
#                 self.data[idx], self.data[p], idx = self.data[p], \
#                                                     self.data[idx], p
#             else:
#                 break
#
#     def remove(self):
#         assert self.length != 0
#         idx = self.length - 1
#
#         poped_value = self.data[0]
#         last_value = self.data[idx]
#         self.length -= 1
#         self.data[0] = last_value
#         idx = 0
#         while idx < self.length:
#             c = (idx) * 2 + 1
#             if c < self.length - 1 and self.data[c] > self.data[c + 1]:
#                 c = c + 1
#             if c >= self.length:
#                 break
#             if c < self.length and self.data[idx] > self.data[c]:
#                 self.data[idx], self.data[c], idx = self.data[c], \
#                                                     self.data[idx], c
#                 continue
#             else:
#                 break
#
#         self.data[self.length] = None
#         return poped_value
#
#
# def solution(scoville, K):
#     answer = 0
#     heap = BinHeap()
#     for s in scoville:
#         heap.insert(s)
#     while heap.data[0] < K and heap.length != 0:
#         if heap.length == 1:
#             return -1
#         # print(heap.data)
#         first = heap.remove()
#         second = heap.remove()
#         heap.insert(first + (2 * second))
#         answer += 1
#     if heap.data[0] < K or heap.length == 0:
#         return -1
#     return answer
#
#
# def test_solution():
#     assert solution([10, 2, 12, 9, 3, 1], 7) == 2
#     assert solution([1, 2, 3, 9, 10, 12], 11) == 3
#     assert solution([1, 2, 3, 9, 10, 12], 1) == 0
#     assert solution([0, 0, 0], 1) == -1
#     assert solution([1, 1], 4) == -1
#     assert solution([10, 15], 40) == 1
#     assert solution([1, 2, 3, 10, -4], 0) == 2
#     assert solution([1, 1, 1, 1, 1], 100) == -1
#     assert solution([10, 15, 11, 1, 0, 5], 5) == 2
#     assert solution([100, 100, 100, 0, 0], 1) == 2
#     assert solution([100, 99], 100) == 1
#     assert solution([1, 1, 1, 1, 3], 5) == 4
#     assert solution([0, 0, 1], 1) == 2
#     assert solution([0, 0, 1], 2) == 2
#     assert solution([0, 0, 1], 3) == -1
#     assert solution([1], 1) == 0
#     assert solution([1], 2) == -1
#     assert solution([-1, -1, -100], 0) == -1
# test_solution()
