import unittest

def recursion_func(cnt):
    if cnt >= 990:
        return
    recursion_func(cnt + 1)
class MyTestCase(unittest.TestCase):
    def test_something(self):
        recursion_func(0)