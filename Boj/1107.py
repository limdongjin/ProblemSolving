import sys
input = sys.stdin.readline

def main():
    target = int(input())
    m = int(input())
    buttons = [True for _ in range(10)]
    if m != 0:
        for t in [int(_) for _ in input().split()]:
            buttons[t] = False

    if target == 100:
        print(0)
        exit()
    elif m == 0:
        print(min(abs(target - 100), len(str(target))))
        exit()
    elif m == 10:
        print(abs(target - 100))
        exit()
    tmp = abs(target - 100)

    for d in range(0, abs(target - 100)):
        lef = is_possible(target - d, buttons)
        rig = is_possible(target + d, buttons)
        if lef:
            ret = abs(d) + len(str(target-d))
            ret = tmp if ret > tmp else ret
            print(ret)
            exit()
        elif rig:
            ret = abs(d) + len(str(target+d))
            ret = tmp if ret > tmp else ret
            print(ret)
            exit()

    print(abs(target-100))


def is_possible(num, buttons):
    if num < 0:
        return False
    if num == 0:
        return buttons[num]

    while num != 0:
        c = num % 10
        num //= 10

        if not buttons[c]:
            return False

    return True

main()