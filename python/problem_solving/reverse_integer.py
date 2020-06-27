def reverse(x: int) -> int:
    if x >= 2 ** 31 - 1 or x <= -2 ** 31:
        return 0
    num = int(str(abs(x))[::-1])
    if int(num) >= 2 ** 31 - 1 or int(num) <= -2 ** 31:
        return 0
    if x < 0:
        return num * -1
    else:
        return num

print(reverse(-31))