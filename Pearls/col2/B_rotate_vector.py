from math import gcd

def simple_rotate(s, rotdist):
    print('simple_rotate')
    assert type(s) == list
    
    n = len(s)

    tmp = s[:rotdist]
    for j in range(rotdist, n):
        s[j-rotdist] = s[j]
    for j in range(rotdist):
        s[n-rotdist+j] = tmp[j]
    print('ret=', s)
    return s

def juggling_rotate(s, rotdist):
    print('juggling_rotate')
    assert type(s) == list
    n = len(s)

    for i in range(gcd(n, rotdist)):
        t = s[i]
        j = i
        
        while True:
            k = j + rotdist
            if k >= n: k -= n
            if k == i: break
            s[j] = s[k]
            j = k
        s[j] = t
    print('ret=',s)
    return s

def rotate_with_reverse(s, rotdist):
    print('rotate with reverse')
    def reverse(a, start, end):
        while start < end:
            a[start], a[end] = a[end], a[start]
            start, end = start+1, end-1

    n = len(s)
    
    reverse(s, 0, rotdist-1)
    reverse(s, rotdist, n-1)
    reverse(s, 0, n-1)

    print('ret=', s)
    return s

def test_rotate():
    input_s = ['a','b','c','d','e','f','g','h']
    input_rotdist = 3
    expected = ['d','e','f','g','h','a','b','c']
    assert simple_rotate(input_s[:], input_rotdist) == expected
    assert juggling_rotate(input_s[:], input_rotdist) == expected
    assert rotate_with_reverse(input_s[:], input_rotdist) == expected
    print('test success')

test_rotate()
