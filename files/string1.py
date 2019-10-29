
def check_characters():
    text = input("please input a text")

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


def acronym():
    text = input("Please enter a text")
    words = text.split(" ")
    result = ""
    for w in words:
        result += w[0:1].upper()
    print(result)




def word_count():
    text = input("Please enter a text\n")
    words = text.split(" ")
    for w in words:
        count = text.count(w)
        print("{0}: {1}".format(w,count))
        count = 0

def encrypt(plain, key):
    cipher = ""
    for c in plain:
        cipher += chr(ord(c) + key)
    print(cipher)

def decrypt(cipher, key):
    plain = ""
    for c in cipher:
        plain += chr(ord(c) - key)
    print(plain)

text = input("Enter your message:\n")
key = int(input("Enter the key: "))
decrypt(text, key)












#word_count()
#acronym()



#check_characters()
