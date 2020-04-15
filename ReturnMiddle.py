def get_middle(s):
    how_big = len(s)
    if how_big % 2 == 0:
        return s[int(how_big/2) - 1] + s[int(how_big/2)]
    else:
        return s[int(how_big/2)]
