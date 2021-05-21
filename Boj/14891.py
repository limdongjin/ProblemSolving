import sys
input = sys.stdin.readline

def solve(topps, K, topp_dirr):
    for topp_id, d  in topp_dirr:
        topps = rotate_topp(topps, topp_id-1, d)

    return calc_score(topps)

def calc_score(topps):
    ret = topps[0][0]*1 + topps[1][0]*2 + topps[2][0]*4 + topps[3][0]*8
    return ret

def rotate_topp(topps, topp_id, d):

    def rotate_one(arr, d):
        if d == 0:
            return arr
        if d == 1:
            return arr[-1:]+arr[:-1]
        if d == -1:
            return arr[1:]+arr[:1]

    rotation = [0]*4
    check = [False]*4
    def set_rotation_table(t_id, d):
        rotation[t_id] = d
        check[t_id] = True

        # left
        left = t_id - 1
        if left>=0 and not check[left]:
            if topps[t_id][6] == topps[left][2]:
                set_rotation_table(left, 0)
            else:
                set_rotation_table(left, -d)

        # right
        right = t_id + 1
        if right<4 and not check[right]:
            if topps[t_id][2] == topps[right][6]:
                set_rotation_table(right, 0)
            else:
                set_rotation_table(right, -d)

    set_rotation_table(topp_id, d)
    for i in range(len(topps)):
        topps[i] = rotate_one(topps[i], rotation[i])
    return topps


topps = [list(int(ch) for ch in input().rstrip()) for _ in range(4)]
K = int(input())
topp_dirr = [list(map(int, input().split())) for _ in range(K)]

print(solve(topps, K, topp_dirr))