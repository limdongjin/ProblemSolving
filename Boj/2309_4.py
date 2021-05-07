import itertools
import sys
input = sys.stdin.readline

def main():
    NINE = 9
    heights = []
    for _ in range(NINE):
        heights.append(int(input()))
    heights.sort()

    sum_h = sum(heights)
     
    combinations_h = itertools.combinations(heights, 2)
    
    for a, b in combinations_h:
        if sum_h - a - b == 100:
            print('\n'.join([str(h) for h in heights
                                if h != a and h != b]))
            break

main()
