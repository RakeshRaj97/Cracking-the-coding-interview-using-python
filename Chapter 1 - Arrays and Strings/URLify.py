# method to replace white spaces with '%20'

def urlify(str, len):
    string = str[0:13]
    string = string.replace(" ", "%20")
    return string


print(urlify("Mr John Smith   ", 13))
