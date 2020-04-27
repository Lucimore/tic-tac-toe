sentence = input().split()
tmp = []
for x in sentence:
    if x.endswith('s'):
        tmp.append(x)
print('_'.join(tmp))