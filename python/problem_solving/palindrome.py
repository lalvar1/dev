from collections import deque


def pal_checker(string):
    char_deque = deque()

    for ch in string:
        char_deque.appendleft(ch)

    still_equal = True

    while len(char_deque) > 1 and still_equal:
        first = char_deque.pop()
        last = char_deque.popleft()
        if first != last:
            still_equal = False

    return still_equal


def pal_int(int):
    return str(int) == str(int)[::-1]

def pal(string):
    return string == string[::-1]

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
print(pal_checker("ojo"))
print(pal_checker("reconocer"))

print(pal("lsdkjfskf"))
print(pal("radar"))
print(pal("ojo"))
print(pal("reconocer"))
