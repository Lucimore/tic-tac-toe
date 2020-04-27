dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
sentence = input().split()
counter = 0
for x in sentence:
    if x not in dictionary:
        print(x)
        counter += 1
if counter == 0:
    print('OK')
