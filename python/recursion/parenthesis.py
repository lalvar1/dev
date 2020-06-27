# def generate_parenthesis(N):
#     if N == 0:
#         return ['']
#     ans = []
#     for c in range(N):
#         for left in generate_parenthesis(c):
#             for right in generate_parenthesis(N - 1 - c):
#                 ans.append('({}){}'.format(left, right))
#     return ans

def generateParenthesis(N):
    ans = []

    def backtrack(S='', left=0, right=0):
        if len(S) == 2 * N:
            ans.append(S)
            return
        if left < N:
            backtrack(S + '(', left + 1, right)
        if right < left:
            backtrack(S + ')', left, right + 1)

    backtrack()
    return ans


print(generateParenthesis(2))