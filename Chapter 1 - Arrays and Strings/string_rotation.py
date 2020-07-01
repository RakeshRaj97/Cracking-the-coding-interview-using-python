# method to find whether a string is a substring of another string
def string_rotation(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        return isSubstring(string1 + string1, string2)


def isSubstring(s1, s2):
    if s1.find(s2):
        return True
    else:
        return False


print(string_rotation('waterbottle', 'erbottlewat'))
