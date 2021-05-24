
def maxsum_slow(a):
    print('maxsum_slow')
    n = len(a)
    ret = 0
    for i in range(n):
        for j in range(i, n):
            # get [i, j] sum
            ret = max(ret, sum(a[k] for k in range(i, j+1)))
    print('ret=', ret)
    return ret

def maxsum_fast1(a):
    # O(N^2)
    print('maxsum_fast1')
    n = len(a)

    # build accsum table
    accsum = [0]*n
    for i in range(n):
        accsum[i] += accsum[i-1] + a[i]

    ret = 0
    for i in range(n):
        for j in range(i, n):
            s = accsum[j] - accsum[i-1]*(i>0)
            ret = max(ret, s)

    print('ret=', ret)
    return ret

def maxsum_fast2(a):
    # O(NlogN) using recursive
    print('maxsum_fast2')

    def maxsum_recursive(left, right):
        if left > right:
            return 0
        if left == right:
            return max(0, a[left])

        mid = (left+right)//2

        # crossing left
        t = lmax = 0
        for i in range(mid, left-1, -1):
            t += a[i]
            lmax = max(t, lmax)

        # crossing right
        t = rmax = 0
        for i in range(mid+1, right+1):
            t += a[i]
            rmax = max(t, rmax)

        return max(lmax+rmax, maxsum_recursive(left, mid), maxsum_recursive(mid+1, right))

    n = len(a)
    ret = maxsum_recursive(0, n-1)
    print('ret=', ret)
    return ret


def maxsum_fast3(arr):
    # O(N) Scanning
    print('maxsum_fast3')
    n = len(arr)
    maxendinghere = 0
    ret = 0
    for i in range(0, n):
        # maxendinghere : max sum of [0..i-1]
        maxendinghere = max(0, maxendinghere+arr[i])
        ret = max(ret, maxendinghere)

    print('ret=', ret)
    return ret
def test_maxsum():
    arr = [31,-41,59,26,-53,58,97,-93,-23,84]
    expected = sum(arr[2:7]) # 59+26+-53+58+97
    print(locals())
    print()

    assert maxsum_slow(arr) == expected
    assert maxsum_fast1(arr) == expected
    assert maxsum_fast2(arr) == expected
    assert maxsum_fast3(arr) == expected
    assert maxsum_fast3([-1, -2]) == 0

    print('test success')

test_maxsum()