# put your python code here
grades = input().split()
count_a = 0
for x in grades:
    if x == 'A':
        count_a += 1
answer = count_a / len(grades)
print(round(answer, 2))
