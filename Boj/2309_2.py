import sys
input = sys.stdin.readline
def main():
    hs = []
    for _ in range(9):
        hs.append(int(input()))
    hs.sort()
    sumh = sum(hs)
    f, s = 0, 0
    for i in range(9):
        for j in range(i+1, 9):
            if sumh - hs[i] - hs[j] == 100:
                f, s = i, j
     
    print('\n'.join([str(hs[i]) for i in range(9) 
        if i != f and i != s]))
    

main()
