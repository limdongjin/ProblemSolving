

def test_solution():
    assert solution2(10, [1,3,4,1,3,1]) == [1,3,4,2,5,6]

def solution(k, room_number):
    ans = []
    dic = {}
    for num in room_number:
        ans.append(find_empty_room(num, dic))
    return ans

def find_empty_room(num, dic):
    if num in dic.keys():
        # find next empty room
        ret = find_empty_room(dic[num], dic)
        dic[num] = ret+1

        return ret

    # num is empty room
    dic[num] = num+1
    return num

def solution2(k, room_number):
    ans = []
    dic = {}

    for num in room_number:
        n, rooms = num, [num]
        while n in dic:
            n = dic[n]
            rooms.append(n)

        ans.append(n)
        for room in rooms:
            dic[room] = n+1

    return ans

test_solution()