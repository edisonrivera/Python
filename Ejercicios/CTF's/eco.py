def eco (word):
    start = 0
    while start < len(word):
        print (word[start:], end = "... ")
        start += 1
    print (end = "\n")
    
while True:
    word = input("-> PALABRA: ")
    if word == "exit":
        break
    eco(word)