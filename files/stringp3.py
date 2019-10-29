def word_count():
    text = input("Please enter a text\n")
    words = text.split(" ")
    for w in words:
        count = text.count(w)
        print("{0}: {1}".format(w,count))
        count = 0


word_count()
