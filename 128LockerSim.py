while True:
    try:


        #iterate through all 128 lockers; accquire factors of locker no. b/t 1 and studentnum. If odd = O, even=X
        StudentNumber = int((input('Student Number (1-128): '))) #studentnumber
        Lockers = []

        if 1 <= StudentNumber <= 128: 
        
            for i in range(1,129):
                factors = 0
                for y in range(1, StudentNumber+1):
                    if i % y == 0:
                        factors += 1 #+= increments
                if factors % 2 == 0:
                    Lockers.append('X')
                else:
                    Lockers.append('O')
              
            for n in range(0, len(Lockers), 8):
                print(*Lockers[n:n+8], sep = ' ')

        elif StudentNumber == 0:
            print('cyas')
            break

        else:
            print('invalid number, must be between 1-128')
    except:
        print('invalid, enter an integer between 1-128')

