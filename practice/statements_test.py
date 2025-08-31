st = 'Print only the words that start with s in this sentence'
split_st = st.split()
filtered_split = [word for word in split_st if word.startswith('s')]
print(filtered_split)

even_nos_ten = [num for num in range(0, 11) if num % 2 == 0]
print(even_nos_ten)

list_hundred_nos = [num for num in range(1, 101)]
for num in list_hundred_nos:
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

st = 'Create a list of the first letters of every word in this string'
res = [word[0] for word in st.split()]
print(res)