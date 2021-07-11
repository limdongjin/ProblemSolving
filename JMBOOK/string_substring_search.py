
# string search part
# p644 ~ 

def naive_search(H, N):
    ret = []
    for start in range(0, len(H)-len(N)+1):
        flag = True
        for i in range(len(N)):
            if H[start+i] != N[i]:
                flag = False
                break
        if flag:
            ret.append(start)
    return ret

def test_solve():
    assert naive_search("hogwarts", "gwart") == [2]

test_solve()
