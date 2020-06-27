def letterCombinations(digits):
    def combine(pres, dicts, digit):
        letL = []
        for pre in pres:
           #letL.append([pre+letter for letter in dicts[digit]])
            for letter in dicts[digit]:
                letL.append(pre + letter)
        return letL

    if digits == '':
        return []
    dicts = {'1': [''], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'],
             '0': [' ']}
    lets = ['']
    for digit in digits:
        # lets=[[pre+letter for letter in dicts[digit]] for pre in lets]
        lets = combine(lets, dicts, digit)
    return lets

print(letterCombinations('233'))

