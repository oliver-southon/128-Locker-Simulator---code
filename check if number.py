ShouldContinue = True
while ShouldContinue:
    UserInput = input('Input pls: ')
    periods = UserInput.count('.')

    if periods == 1 in UserInput:
        val = float(UserInput)
        print(val, "Yes, user input is a float number.")
    elif UserInput == '0':
        print('bye')
        ShouldContinue = False
    elif UserInput.isnumeric():
        val = int(UserInput)
        print(val, "Yes, input string is an Integer.")
    else:
        print(UserInput, 'is a string lol')
