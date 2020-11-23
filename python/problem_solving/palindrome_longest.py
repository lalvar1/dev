class Solution2:
    def longestPalindrome_brute_force(self, s: str) -> str:
        def isPalindrome(s):
            if s is "":
                return False
            for i in range(len(s) // 2):
                if s[i] != s[-1 - i]:
                    return False
            return True

        common_subs = {}

        if s is "":
            return ""

        for i in range(len(s)):
            for j in range(1, len(s) + 1):
                # if s[i:j] == s[i:j][::-1]:
                if isPalindrome(s[i:j]):
                    common_subs[s[i:j]] = len(s[i:j])

        return max(common_subs, key=common_subs.get)

    def longestPalindrome_best(self, s: str) -> str:
        if s is '':
            return s
        max_len = 0
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandFromCenter(s, i, i)
            len2 = self.expandFromCenter(s, i, i + 1)
            l = max(len1, len2)
            if l > end - start:
           # if l > 1:
                start = i - (l - 1) // 2
                end = i + l // 2

        return s[start:end + 1]

    def expandFromCenter(self, s, idx1, idx2):
        while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
            idx1 -= 1
            idx2 += 1
        return idx2 - idx1 - 1


# a = Solution2()
# palindrome = 'babad'
# palindrome = 'cbbd'
# print(a.longestPalindrome_best(palindrome))

def longestPalindrome(string):
    if len(string) == 0:
        return ''
    # palindromes_list = set()
    # palindromes_list |= {getPalindromeAt(i, string) for i in range(len(string))}
    palindromes_list = [getPalindromeAt(i, string) for i in range(len(string))]
    # max_length = max(palindromes_list)
    # max_index = palindromes_list.index(max_length)
    # start = max_index - max_length // 2
    # end = max_index + max_length // 2 + 1
    # return string[start:end]
    return max(palindromes_list, key=len)


# def getPalindromeAt(position, string):
#     longest = (position, position)
#     for lower, upper in [(position - 1, position + 1), (position, position + 1)]:
#         while lower >= 0 and upper < len(string) and string[lower] == string[upper]:
#             upper += 1
#             lower -= 1
#         longest = max(longest, (lower + 1, upper - 1), key=lambda a: a[1] - a[0])
#     return string[longest[0]: longest[1] + 1]

def getPalindromeAt(position, string):
    # longest = []
    # lower = upper = position
    longest = 1
    start = 0
    for lower, upper in [(position-1, position), (position-1, position+1)]:
        while lower >= 0 and upper < len(string) and string[lower] == string[upper]:
            upper += 1
            lower -= 1
            if upper - lower + 1 > longest:
                start = lower
                longest = upper - lower + 1
    return upper - lower - 1


def longest_pal(string):
    max_length = 1
    start = 0
    length = len(string)
    for i in range(1, length):
        # Find the longest even and odd length palindrome with center points as i-1 and i and i-1 i+1 respectively.
        for low, high in [(i - 1, i), (i - 1, i + 1)]:
            while low >= 0 and high < length and string[low] == string[high]:
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1
    return string[start:start+max_length]


def brute_force(s):
    if s == "":
        return s
    common = set()
    for i in range(len(s)):
        for j in range(1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                common |= {s[i:j]}
                #common[s[i:j]] = len(s[i:j])
    return max(common, key=len)


palindrome = 'babad'
#palindrome = 'a'
print(longest_pal(palindrome))
print(brute_force(palindrome))

string = 'babad'
start = 0
max_length = 1
for i in range(1, len(string)):
    for low, high in [(i-1, i), (i-1, i+1)]:
        while low >=0 and high < len(string) and string[low]==string[high]:
            if high-low+1 > max_length:
                max_length = high-low+1
                start = low
            low-=1
            high-=1
print(string[start:start+max_length])
