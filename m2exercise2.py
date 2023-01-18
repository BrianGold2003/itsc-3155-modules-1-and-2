phrase = input("Please enter a phrase or word: ").strip()
for element in phrase:
    if element.islower():
        print(element, end = '')
for element in phrase:
    if element.isupper():
        print(element, end = '')