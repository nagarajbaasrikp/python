for i in range(0, 11, 2):
    print(i)

#enumerate
index_count = 0
for letter in 'abcde':
    print('The letter at index {} is {}'.format(index_count, letter))
    index_count += 1
word = 'abcde'
index_count = 0
for item in enumerate(word):
    print(item)
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
for item in zip(l1, l2):
    print(item)