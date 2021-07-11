
def merge(a, p, q, r):
    L, R = a[p:q+1]+[float('inf')], a[q+1:r+1]+[float('inf')]
    # ASSERT L is sorted
    # ASSERT R is sorted

    i, j = 0, 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
            continue
        a[k] = R[j]
        j += 1

# @param a : array
# @param p : start index (inclusive)
# @param r : end   index (inclusive)
def merge_sort(a, p, r):
    if p >= r:
        return
    q = (p+r)//2
    merge_sort(a, p, q)
    merge_sort(a, q+1, r)
    merge(a, p, q, r)


def main():
    A = [10, 9, 1, 8, 11, 3, 2, 8,7, 4, 6, 5]
    merge_sort(A, p=0, r=len(A)-1)
    print(A)


main()
