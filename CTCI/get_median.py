import heapq


class GetMedian:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def get(self):
        left_len = len(self.left_heap)
        right_len = len(self.right_heap)
        if left_len == right_len == 0:
            return 999999 # error code

        if left_len >= right_len:
            return heapq.nsmallest(1, self.left_heap)[0][1]
        else:
            return heapq.nsmallest(1, self.right_heap)[0][1]

    def balancing(self):
        diff_len = len(self.left_heap) - len(self.right_heap)
        if diff_len >= 2:
            priority, num = heapq.heappop(self.left_heap)
            self.push_right(num)
        elif diff_len <= -2:
            priority, num = heapq.heappop(self.right_heap)
            self.push_left(num)

    def push_left(self, num):
        heapq.heappush(self.left_heap, (-num, num))

    def push_right(self, num):
        heapq.heappush(self.right_heap, (num, num))

    def get_leftmax(self):
        # 주의 : left_heap 은 개념적으로는 최대힙이 되도록 구현했지만
        #       내부적으로는 최소힙으로 구성된것이다.
        return heapq.nsmallest(1, self.left_heap)[0][1]

    def add_number(self, num):
        if not self.left_heap and not self.right_heap:
            self.push_left(num)
            return

        max_left = self.get_leftmax()

        if num < max_left:
            self.push_left(num)
        else:
            self.push_right(num)

        self.balancing()


inp = [1, -1, 10, 5, 8, -5, 3, 6, 7, 20, -10]
get_median = GetMedian()
for i, num in enumerate(inp):
    get_median.add_number(num)
    median_value = get_median.get()
    expected = sorted(inp[:i + 1])[i // 2]
    print('inputs = ', inp[:i + 1])
    print('expected = ', expected, ' actual = ', median_value)
    assert expected == median_value
