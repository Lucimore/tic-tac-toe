text = input()
words = text.lower().split()
tmp = []
counter = 0
for word in words:
    if word.startswith(('https://', 'http://', 'www.')):
        tmp.append(counter)
    counter += 1
final = text.split()
for x in tmp:
    print(final[x])
