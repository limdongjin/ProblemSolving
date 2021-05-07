
def main():
    hs = []
    for _ in range(9):
        hs.append(int(input()))
    
    hs.sort()
    select = [0]*2 + [1]*7
    while True:
        if is_ans(hs, select):
            print('\n'.join([str(hs[i]) for i in range(9)
                                    if select[i]]))
            break
        if not next_perm(select):
            break

def is_ans(hs, select):
    return sum([hs[i] for i in range(9)
                if select[i]]) == 100

def next_perm(a):
    def reverse_inplace(a, start, end):
        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1
    n = len(a)
    
    # find i
    i = n - 1
    while i > 0 and not (a[i-1] < a[i]):
        i -= 1
    if i == 0:
        return False

    # find j. bigger than a[i-1]
    def find_first_bigger(seq, target):
        j = n - 1
        while j > 0 and not (seq[j] > seq[i-1]):
            j -= 1
        return j

    j = find_first_bigger(a, a[i])
    
    # swap
    a[i-1], a[j] = a[j], a[i-1]

    reverse_inplace(a, i, n-1)
    
    return True
main()
