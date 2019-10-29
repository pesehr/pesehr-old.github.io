def check_characters():
    text = input("please input a text\n")

    upper_case, lower_case, digit, symbol = 0,0,0,0

    for c in text:
        if c.isupper():
            upper_case += 1
        elif c.islower():
            lower_case += 1
        elif c.isdigit():
            digit += 1
        else :
            symbol += 1

    result = "upper case:{0}, lower case:{1}, digit: {2}, symbols: {3}".format(upper_case, lower_case, digit, symbol)
    print(result)


check_characters()
