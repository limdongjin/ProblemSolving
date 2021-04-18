import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        import datetime
        N = 100000000
        start = datetime.datetime.now()
        nums = []
        for i in range(N):
            nums.append(i)
        ret = []
        for i in range(N - 1, -1, -1):
            ret.append(nums[i])
        end = datetime.datetime.now()
        print('for-loop : ', (end-start).total_seconds())

        start = datetime.datetime.now()
        nums = [i for i in range(N)]
        ret = nums[::-1]
        end = datetime.datetime.now()
        print('comprehension : ', (end-start).total_seconds())