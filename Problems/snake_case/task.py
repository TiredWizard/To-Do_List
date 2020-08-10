word = input()
new_word = ""

for x in word:
    if x.isupper():
        new_word += "_{0}".format(x.lower())
    else:
        new_word += "{0}".format(x)
print(new_word)
