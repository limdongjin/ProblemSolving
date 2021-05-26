

def test_ans():
    A = [1,2,3, 3, 4, 5]
    M = 3
    expected = [2.0, 8/3, 10/3, 12/3]
    
    assert moving_average1(A, M) == expected 
    assert moving_average2(A, M) == expected 


def moving_average1(A, M):
    # O(NM)
    ret = []

    for i in range(M-1, len(A)):
        partial_sum = sum(A[i-j] for j in range(0, M))
        print(i, partial_sum)
        ret.append(partial_sum / M)
    
    print(ret)
    return ret

def moving_average2(A, M):
    # O(N)
    prev_sum = sum(A[:M])
    ret = [prev_sum/M]
    
    for i in range(M, len(A)):
        prev_sum = prev_sum - A[i-M] + A[i]
        ret.append(prev_sum/M)
    
    print(ret)
    return ret
test_ans()
