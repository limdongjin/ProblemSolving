from unittest import TestCase


class Test(TestCase):
    def test_main(self):
        from datetime import datetime
        items = [str(_) for _ in range(100000000)]

        print('start comparision')

        start = datetime.now()
        for item in items:
            len(item)
        end = datetime.now()
        print('global len(): ', (end-start).total_seconds())

        start = datetime.now()
        local_len = len
        for item in items:
            local_len(item)
        end = datetime.now()
        print('local_len()', (end-start).total_seconds())

        # almost same time
