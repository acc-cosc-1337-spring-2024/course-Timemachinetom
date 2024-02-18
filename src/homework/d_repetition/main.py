import repetition

option = 0
quit = False

while quit != True:
    option = input ("Homework 3 Menu\n1-Factorial\n2-Sum odd numbers\n3-Exit")
    option = int(option)

    while option == 1:
        num = input ("Enter a whole number between 1 and 10")
        num = int(num)
        if num >=1 and num <= 10:
            factorial = repetition.get_factorial(num)
            print(factorial)
            exit = input ("Do you want to exit>\n1 - Yes\n2 - no")
            exit = int(exit)
            if exit == 1:
                exit = 0
                option = 0
                quit = True
            elif exit == 2:
                exit = 0
                option = 0
        elif num <1 or num > 10:
            print("(num) is not a valid number. Please enter a whole number between 1 and 10.")
            option = int(1)
            
    while option == 2:
        num = input ("Enter a whole number between 1 and 100")
        num = int(num)
        if num >=1 and num <= 100:
            sum = repetition.sum_odd_numbers(num)
            print(sum)
            exit = input ("Do you want to exit>\n1 - Yes\n2 - no")
            exit = int(exit)
            if exit == 1:
                exit = 0
                option = 0
                quit = True
            elif exit == 2:
                exit = 0
                option = 0
        elif num <1 or num > 100:
            print("(num) is not a valid number. Please enter a whole number between 1 and 100")
            option = int(2)
            
    while option == 3:
        exit = input ("Are you sure you want to exit?\n1 - Yes\n2 - No")
        exit = int(exit)
        if exit == 1:
            exit = 0
            option = 0
            quit = True
        elif exit == 2:
            exit = 0
            option = 0
