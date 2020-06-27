def lengthOfLongestSubstring(s):
    str_list = []
    max_length = 0
    for x in s:
        if x in str_list:
            str_list = str_list[str_list.index(x) + 1:]
        str_list.append(x)
        max_length = max(max_length, len(str_list))
    return max_length


def lengthOfLongestSubstring_quickest(s):
    dicts = {}
    maxlength = start = 0
    for i,value in enumerate(s):
        if value in dicts:
            sums = dicts[value] + 1
            if sums > start:
                start = sums
        num = i - start + 1
        if num > maxlength:
            maxlength = num
        dicts[value] = i
    return maxlength


# THIS
def lengthOfLongestSubstring_other(s):
    d = f = ""
    for i, val in enumerate(s):
        if val not in f:
            f += val
        else:
            if len(d) < len(f):
                d = f           # d=historical max length
            f = f[f.index(val)+1:] + val
    return max(len(d), len(f))


#"asjrgapa"

print(lengthOfLongestSubstring("asjrgapa"))
string = 'asjrgapa'

largest = ''
max_length = 0
largets = set()
for ch in string:
    if ch in largest:
        largest = largest[largest.index(ch)+1:]
    largest += ch
    largets |= {largest}
    max_length = max(max_length, len(largest))
print(max_length, max(largets, key=len))




























