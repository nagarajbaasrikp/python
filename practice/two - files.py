#old way - need to manually close file
myfile = open('myfile.txt')
text = myfile.read()
print(text)
text_again = myfile.read()
print(f'Trying to read without using seek to jump back to the beginning of the file: {text_again}')
myfile.seek(0)
text_again = myfile.read()
print(text_again)
text_again_test = text_again.split('\n')
myfile.seek(0)
read_lines_myfile = myfile.readlines()
print(text_again_test == read_lines_myfile)
print(text_again_test, '\t', read_lines_myfile)
myfile.close()
#my404_file = open('NA.txt')
#new way
with open('myfile.txt') as my_new_file:
    file_contents = my_new_file.read()
    print(file_contents)
with open('myfile.txt', mode = 'a+') as f:
    f.write('\nthis is the added fourth line')
    new_file_contents = f.read()
    print(new_file_contents)