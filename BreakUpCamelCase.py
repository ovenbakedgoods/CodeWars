#Separates Camel case input with a string
def solution(s):
    newwords = []
    for i in s:
        if i.islower():
            newwords.append(i)
        else:
            newwords.append(" " + i)

    return ''.join(newwords)
