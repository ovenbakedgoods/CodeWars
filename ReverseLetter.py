#Remove any non alphabetic characters and reverse and return string.
def reverse_letter(string):
    newone = []
    for i in string:
        if i.isalpha():
            newone.append(i)
        stringnew = ''.join(newone)

    return stringnew[::-1]
