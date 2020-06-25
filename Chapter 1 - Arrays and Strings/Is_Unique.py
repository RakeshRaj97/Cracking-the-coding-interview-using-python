text = input("Enter the string: ")

new_list = []
for char in text:
    if char in new_list:
        print("False")
        break

    else:
        new_list.append(char)
