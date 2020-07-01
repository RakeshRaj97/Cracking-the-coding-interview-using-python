# method to find whether a string is a substring of other

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        return isSubstring(s1 + s1, s2)


def isSubstring(string, sub):
    if string.find(sub):
        return True
    else:
        return False


print(string_rotation('waterbottle', 'erbottlewat'))
print(string_rotation('hello', 'he'))
