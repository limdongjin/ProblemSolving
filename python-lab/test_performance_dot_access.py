import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        from datetime import datetime
        N = 100000000
        start = datetime.now()
        l = []
        for i in range(N):
            l.append(i)
        end = datetime.now()
        print('l.append access(dot): ', (end-start).total_seconds())

        start = datetime.now()
        l2 = []
        append = l2.append
        for i in range(N):
            append(i)
        end = datetime.now()
        print('append access(alias l2.append): ', (end-start).total_seconds())

        # almost same!

# if __name__ == '__main__':
#     unittest.main()
