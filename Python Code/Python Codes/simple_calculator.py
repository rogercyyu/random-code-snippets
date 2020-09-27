# simple calculator

print('SIMPLE CALCULATOR'.center(30, '-'))

# check for valid number
def inputNumber(message):
    while True:
        try:
            num = float(input(message))
        except ValueError:
            print("That is not a number.")
            continue
        else:
            return num
            break

def Calculator():
    # ask user for numbers
    num_1 = inputNumber('What is the first number?: ')
    num_2 = inputNumber('What is the second number?: ')

    # ask user for operation?
    choice = input('What operation? (add,subtract,divide or multiply): ')

    while choice not in ('add','subtract','multiply','divide'):
        print('Please put in a correct operation.')
        choice = input()

    if choice == 'add':
        ans = num_1 + num_2
    elif choice == 'subtract':
        ans = num_1 - num_2
    elif choice == 'multiply':
        ans = num_1*num_2
    elif choice == 'divide':
        ans = num_1/num_2
    print('The answer is: ' +str(ans))

#tryagain?
while True:
    Calculator()
    while True:
        answer = input('Would you like to continue? (y/n): ')
        if answer in ('y','n'):
            break
    if answer == 'n':
        break
    print('Reseting...')
        
