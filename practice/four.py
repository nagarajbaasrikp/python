#reverse a sentence
sentence = 'this is a test sentence'
new_sentence = ' '.join(sentence.split()[::-1])
print(new_sentence)

#check if list has 3 next to 3
my_list = [1, 2, 3, 4, 5, 6]
my_other_list = [1, 2, 3, 3, 5, 6]

def three_by_three(arg_list):
    for i in range(0, len(arg_list) - 1):
        if arg_list[i] == arg_list[i + 1] == 3:
            return True
    return False

print(three_by_three(my_list))
print(three_by_three(my_other_list))

#find 007

def spy_game(my_list):
    joined_list = ''.join([str(num) for num in my_list])
    if('007' in joined_list):
        return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))