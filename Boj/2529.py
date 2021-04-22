
boo = []
ans = []
check = []

def main():
    global boo, check, ans
    k = int(input())
    boo = input().split()
    check = [False for _ in range(10)]

    go(idx=0, num="")
    ans.sort()
    print(ans[-1])
    print(ans[0])

def is_possible(num):
    global boo
    for i in range(len(num) - 2, -1, -1):
        if boo[i] == '<' and int(num[i]) > int(num[i+1]):
            return False
        elif boo[i] == '>' and int(num[i]) < int(num[i+1]):
            return False
    return True

def go(idx, num):
    if idx == len(boo) + 1:
        global ans
        ans.append(num)
        return

    for i in range(0, 10):
        if check[i]:
            continue
        check[i] = True
        if is_possible(num+str(i)):
            go(idx+1, num+str(i))
        check[i] = False


main()