

def get_anagrams(target, words):
    print('get_anagrams')

    def preprocessing(a):
        d = {}
        for word in a:
            label = ''.join(sorted(word))

            if label not in d:
                d[label] = []
            d[label].append(word)
        _ret = sorted([(k, d[k]) for k in d])
        return _ret

    # word_dict[i] = (label, [word1, word2, word3])
    word_dict = preprocessing(words)
    target_label = ''.join(sorted(target))

    # binary search
    low, high = 0, len(word_dict)-1
    ret = {}
    while low <= high:
        mid = (low+high)//2
        if word_dict[mid][0] == target_label:
            ret = word_dict[mid][1]
            break
        elif word_dict[mid][0] < target_label:
            low = mid+1
        else:
            high = mid-1

    print('ret=', ret)
    return ret

def test_anagram():
    words = ['posited','dopiest','gogo','deposit', 'hello', 'world']
    target = 'deposit'
    expected = {'deposit', 'posited', 'dopiest'}

    actual = get_anagrams(target=target, words=words)

    assert len(actual) == len(expected)
    for v in actual:
        assert v in expected

    print('test success')

test_anagram()