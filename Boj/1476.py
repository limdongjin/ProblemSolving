

def main():
    # 15 28 19
    e, s, m = [int(_) for _ in input().split()]

    cnt = 1
    ee, ss, mm = 1, 1, 1
    while True:
        if ee == e and ss == s and mm == m:
            break
        ee, ss, mm = ee + 1, ss + 1, mm + 1
        if ee > 15:
            ee = 1
        if ss > 28:
            ss = 1
        if mm > 19:
            mm = 1
        cnt += 1

    print(cnt)

main()