def upperAndLower (string):
    
    upper, lower = 0, 0
    for i in range(len(string)):
        if string[i].isupper():
            upper += 1
        elif string[i].islower():
            lower += 1

    print(f"There are {upper} upper case letters and {lower} lower case letters in this string")

string = str(input("Type a strng! "))
upperAndLower(string)