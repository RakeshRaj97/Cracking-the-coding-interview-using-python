# given two strings, decide if one is a permutation of the other


str1 = input('')
str2 = input('')


def is_a_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    # sort the strings
    a = sorted(str1)
    b = sorted(str2)

    # compare sorted strings
    for i in range(len(a)):
        if (a[i] != b[i]):
            return False
    return True


if is_a_permutation(str1, str2):
    print("True")
else:
    print("False")
