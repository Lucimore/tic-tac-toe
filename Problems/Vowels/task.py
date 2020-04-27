vowels = 'aeiou'
# create your list here
user_input = input()
vowels_list = [x for x in user_input if x in vowels]
print(vowels_list)
