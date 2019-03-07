#
# https://programmers.co.kr/learn/courses/30/lessons/42577
# 문제 제목: 전화번호 목록
#
def solution(phone_book):
    answer = True
    phone_book_h = {}
    for phone in phone_book:
        phone_book_h[phone] = 1
    k = 0
    for phone in phone_book:
        len_p = len(phone)
        for i in range(len_p):
            if i == k:
                continue
            if phone_book_h.get(phone[:i]) is not None:
                return False
        k += 1
    return True


def test_solution():
    assert solution(["119", "97674223", "1195524421"]) is False
    assert solution(["123","456","789"]) is True
    assert solution(["12","123","1235","567","88"]) is False


test_solution()
