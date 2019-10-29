def acronym():
    text = input("Please enter a text")
    words = text.split(" ")
    result = ""
    for w in words:
        result += w[0:1].upper()
    print(result)


acronym()
