# method to calculate whether a string is a permutation of a palindrome

def is_palin_perm(str):
    #remove the white spaces and lower all the characters
    str = str.replace(" ","")
    str = str.lower()

    #create a dictionary to store key, value pairs of each elements
    d = dict()
    #loop through each element and calculate its count
    for i in str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    #create a variable to store the odd value occurences
    #the maximum number of odd elements in a given palindrom should be atmost 1
    odd_count = 0
    for k, v in d.items():
        if v%2 != 0 and odd_count == 0:
            odd_count += 1
        elif v%2 !=0 and odd_count != 0:
            return False
    return True

print(is_palin_perm("raecrac"))
print(is_palin_perm("This is not a palin permutation"))