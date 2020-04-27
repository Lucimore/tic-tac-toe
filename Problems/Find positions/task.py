# put your python code here
numbers = input().split()
find_me = input()
position = 0
counter = 0
tmp = []

for x in numbers:
    if x == find_me:
        tmp.append(str(position))
        counter += 1
    position += 1
if counter == 0:
    print('not found')
final = " ".join(tmp)
print(final)
