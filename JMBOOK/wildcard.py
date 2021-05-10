import sys
input =sys.stdin.readline

def match(pattern, word):
    n = max(len(pattern), len(word)) + 1
    cache = [[None]*n for _ in range(n)]

    def _memorized_match(p, w):
        if p == len(pattern):
            return w == len(word)
        if cache[p][w] != None:
            return cache[p][w]
        
        # case1. pattern[p] == word[w]. check next chars.
        if p < len(pattern) and w < len(word) and \
                (pattern[p] == word[w] or pattern[p] == '?'):
                    cache[p][w] = _memorized_match(p+1, w+1)
                    return cache[p][w]
        
        # case2. pattern[p] is not star, then not matched
        if pattern[p] != '*':
            cache[p][w] = False
            return cache[p][w]
        
        # case3. pattern[p] is star
        if _memorized_match(p+1, w) or \
                (w < len(word) and _memorized_match(p, w+1)):
            cache[p][w] = True
            return cache[p][w]

        # case4. not matched
        cache[p][w] = False
        return cache[p][w]

    return _memorized_match(0, 0) 


TC = int(input())
for _ in range(TC):
    pattern = input().rstrip()
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input().rstrip())
    words.sort()

    for word in words:
        if match(pattern, word):
            print(word)

