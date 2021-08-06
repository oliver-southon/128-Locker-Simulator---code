ShouldContinue = True

while ShouldContinue:
    string = input("Enter 8 character string ('end' to quit): ")
    if string == 'end':
        ShouldContinue = False
    else:
        f = open('outputs.txt', 'w')
        for z in range(1,129):
       
            Lockers = []
            #the process
            for i in range(1,129):
                factors = 0
                for y in range(1, z+1): #for loop gets no. of factors
                    if i % y == 0:
                        factors += 1 #+= increments
                if factors % 2 == 0:
                    Lockers.append("X")
                else:
                    Lockers.append("O")
            
            #for formatting  
            for n in range(0, len(Lockers), 8):
                print(*Lockers[n:n+8], sep = ' ', file = f)
        f.close()
        
        with open('outputs.txt') as f:
            variable = f.read()
            if string in variable:
                print('is somewhere')
            else:
                print('not in there')
        
        #to write it in
        # f = open('outputs.txt', 'w')
        # print(Lockers)
        # f.close()