# def operation(b, a, op):
#     if op == '+':
#         return int(a) + int(b)
#     if op == '-':
#         return int(a) - int(b)
#     if op == '*':
#         return int(a) * int(b)
#     else:
#         return int(int(a) // int(b))


def evalRPN(A):
    polish_list = []
    for op in A:
        # if op not in ['+', '-', '*', '/']:
        if op not in '+-*/':
            polish_list.append(op)
        else:
            polish_list.append(int(eval('{2}{1}{0}'.format(polish_list.pop(), op, polish_list.pop()))))
    return polish_list[0]


A = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
print(evalRPN(A))
