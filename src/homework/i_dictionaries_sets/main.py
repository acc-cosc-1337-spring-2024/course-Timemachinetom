import sets

option = 0
quit = False
widgets = {}
prog1 = set ({'Student1', 'Student2', 'Student3'})
prog2=  set ({'Student3', 'Student4', 'Student5'})

while quit == False:
    option = input("Homework 7 Menu\n1-Students who took prog1 and prog2\n2-Students who took prog1 or prog2\n3-Students who took prog1 not prog2\n4-Students who took prog2 not prog1\n5-Exit")
    option = int(option)

    while option == 1:
        students = sets.get_students_who_took_prog1_and_prog2 (prog1, prog2)
        print (students)
        exit = input ("Do you want to exit>\n1 - Yes\n2 - no")
        exit = int(exit)
        if exit == 1:
            exit = input ("Are you sure you want to exit?\n1 - Yes\n2 - No")
            exit = int(exit)
            if exit == 1:
                exit = 0
                option = 0
                print("Goodbye")
                quit = True
            else:
                exit = 0
                option = 0
        else:
            exit = 0
            option = 0

    while option == 2:
        students = sets.get_students_who_took_prog1_or_prog2(prog1, prog2)
        print (students)
        exit = input ("Do you want to exit>\n1 - Yes\n2 - no")
        exit = int(exit)
        if exit == 1:
            exit = input ("Are you sure you want to exit?\n1 - Yes\n2 - No")
            exit = int(exit)
            if exit == 1:
                exit = 0
                option = 0
                print("Goodbye")
                quit = True
            else:
                exit = 0
                option = 0
        else:
            exit = 0
            option = 0

    while option == 3:
        students = sets.get_students_who_took_prog1_not_prog_2(prog1,prog2)
        print (students)
        exit = input ("Do you want to exit>\n1 - Yes\n2 - no")
        exit = int(exit)
        if exit == 1:
            exit = input ("Are you sure you want to exit?\n1 - Yes\n2 - No")
            exit = int(exit)
            if exit == 1:
                exit = 0
                option = 0
                print("Goodbye")
                quit = True
            else:
                exit = 0
                option = 0
        else:
            exit = 0
            option = 0

    while option == 4:
        students = sets.get_students_who_took_prog2_not_prog_1(prog1,prog2)
        print (students)
        exit = input ("Do you want to exit>\n1 - Yes\n2 - no")
        exit = int(exit)
        if exit == 1:
            exit = input ("Are you sure you want to exit?\n1 - Yes\n2 - No")
            exit = int(exit)
            if exit == 1:
                exit = 0
                option = 0
                print("Goodbye")
                quit = True
            else:
                exit = 0
                option = 0
        else:
            exit = 0
            option = 0

    while option == 5:
        exit = input ("Are you sure you want to exit?\n1 - Yes\n2 - No")
        exit = int(exit)
        if exit == 1:
            exit = 0
            option = 0
            print("Goodbye")
            quit = True
        else:
            exit = 0
            option = 0
