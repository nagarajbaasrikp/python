print(list(range(0,11)), range(0,11))

#check whether a number is in a given range
def member_of(low, high, num):
    if num in range(low, high +1):
        return True
    return False

print(member_of(2,3,4))
print(member_of(1,10,10))
print(member_of(4, 50, 4))

#palindrome - python style

word1 = 'madam'
word2 = 'madman'

def palindrome(word):
    if word == word[::-1]:
        print('Palindrome')
    else:
        print('Normal Word')

palindrome(word1)
palindrome(word2)

#check if a sentence is a pangram (pangram is a sentence with every word in the alphabet)

pangram = "The quick brown fox jumps over the lazy dog"
sentence = 'This is a normal sentence, non-pangram'

def is_pangram(sentence):
    complete_ascii_values = list(range(97, 123))
    ascii_values = []
    for word in sentence.split():
        for letter in word.lower():
            if ord(letter) not in ascii_values:
                ascii_values.append(ord(letter))
    ascii_values.sort()
    if(ascii_values == list(complete_ascii_values)):
        return True
    else:
        return False

is_pangram(pangram)
is_pangram(sentence)