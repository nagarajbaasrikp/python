#try-except-finally block

while True:
    try:
        def div(num1, num2):
            return num1 /num2
        num1 = int(input('Enter a number'))
        num2 = int(input('Enter another number'))
        print('The result of division is ', div(num1, num2))
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except TypeError:
        print('Enter numbers only!')
    except:
        print('Error!')
    else:
        print('Division carried out successfully!')
        break
    finally:
        print('Finally it is done!')