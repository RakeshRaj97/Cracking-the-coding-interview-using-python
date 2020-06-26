# method to calculate whether two strings are one edit away
def one_away(str1, str2):
    if len(str1) == len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count
    if len(str1) > len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] not in str2:
                count += 1
        return count

    if len(str1) < len(str2):
        count = 0
        for i in range(len(str2)):
            if str2[i] not in str2:
                count += 1
        return count


a = one_away("pae", "pie")
b = one_away("paes", "pae")
c = one_away("pe", "pae")
if a > 1:
    print('false')
else:
    print('true')
if b > 1:
    print('false')
else:
    print("true")
if c > 1:
    print('false')
else:
    print("true")
