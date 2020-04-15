#Simple, returns the shortest word in a sentence. Or multiple sentences if you like
def find_short(s):
    words = s.split(' ')
    return len(min(words, key = len))
