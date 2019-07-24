ShouldContinue = True
while ShouldContinue:
    UserInput = input('Student Number (1-128): ')
    #iterate through all 128 lockers; accquire factors of locker no. b/t 1 and studentnum. If odd = O, even=X
    if UserInput == '0':
        print('cyas')
        ShouldContinue = False

    elif UserInput.isnumeric():
        StudentNumber = int(UserInput) #studentnumber
        Lockers = []

        if 1 <= StudentNumber <= 128: 
            #the process
            for i in range(1,129):
                factors = 0
                for y in range(1, StudentNumber+1): #for loop gets no. of factors
                    if i % y == 0:
                        factors += 1 #+= increments
                if factors % 2 == 0:
                    Lockers.append('X')
                else:
                    Lockers.append('O')
            #for formatting  
            for n in range(0, len(Lockers), 8):
                print(*Lockers[n:n+8], sep = ' ')
        else:
            print("Invalid Number")

    else:
        print("Please enter a number between 1 and 128 inclusive or 0 to end")

