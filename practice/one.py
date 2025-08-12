dict_one = {'one': 1, 'two': 2}
print(dict_one)
keys = dict_one.keys()
print(keys)
values = dict_one.values()
description_values = dict_one.values
print(description_values)
print(dict_one.items())
for item in dict_one.items():
    print(item)
for (key, value) in dict_one.items():
    print(key, value)

#tuples
t = ('a', 'a', 'b')
print(f'The type of t is: {type(t)}')
print('"a" is in the tuple {0} times'.format(str(t.count('a'))))

#sets
my_set = set()
my_set.add(1)
my_set.add(2)
print(f'The elements of my_set are: {my_set}')