# put your python code here
phrase = input().split()
phrases = dict()
for i in phrase:
    word = i.lower()
    b = 0
    count = 0
    while b < len(phrase):
        if word == phrase[b].lower():
            count += 1
        b += 1
    phrases[word] = count

for value in phrases.keys():
    print(value, phrases[value])

