def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """
    words = ''
    for i, word in enumerate(S.split()):
        if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            words += word + 'ma' + 'a' * (i + 1) + ' '
        else:
            words += word[1:] + word[0] + 'ma' + 'a' * (i + 1) + ' '
    return words.rstrip()


def to_goat(S):
    """
    :type S: str
    :rtype: str
    """
    words = []
    for i, word in enumerate(S.split(), 1):
        if word[0] in 'aeiouAEIOU':
            words.append(word + 'ma' + 'a'*i)
        else:
            words.append(word[1:] + word[0] + 'ma' + 'a'*i)
    return ' '.join(words)

print(to_goat("I speak Goat Latin"))
