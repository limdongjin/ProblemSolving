

def main():
    s = input().rstrip()
    cnt = 0
    i = 0 
    dic = {'c=': True, 'c-': True, 'dz=': True, 'd-': True, 'lj': True, 'nj': True, 's=': True, 'z=': True}
    while i < len(s):
        if i == len(s) - 1:
            cnt += 1
            break
        cc = s[i:i+2]
        if cc in dic:
            i += 2
        elif cc == 'dz' and i < len(s) - 2 and s[i:i+3] in dic:
            i += 3
        else:
            i += 1

        cnt += 1
    
    print(cnt)

main()
