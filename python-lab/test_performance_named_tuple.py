import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        from datetime import datetime
        N = 3000

        # N*N 개의 tuple 을 리스트에 저장하고. 요소에 접근하는 시간을 측정한다.
        start = datetime.now()
        items = [(y, x) for x in range(N) for y in range(N)]
        for item in items:
            item[0]
            item[1]

        end = datetime.now()
        tuple_time = (end - start).total_seconds()
        print('tuples : ', tuple_time)
        del items

        # N*N 개의 namedtuple 을 리스트에 저장하고. 요소에 접근하는 시간을 측정한다.
        start = datetime.now()

        from collections import namedtuple
        P = namedtuple('P', 'y x')
        print(id((1,2)), id(P(1,2)), id((2,3)), id(P(2,4)), sep=', ')
        items = [P(y, x) for x in range(N) for y in range(N)]
        for item in items:
            item.x
            item.y
        end = datetime.now()
        namedtuple_time = (end - start).total_seconds()
        print('namedtuple : ', namedtuple_time)
        # 로컬 실행 결과
        # tuples :  1.89178  sec
        # namedtuple :  8.945932  sec

        # namedtuple 의 생성, 접근 속도가 매우 느리다.
        assert namedtuple_time > tuple_time * 2