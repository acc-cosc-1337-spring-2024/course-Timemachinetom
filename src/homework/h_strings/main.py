import strings

option = 0
quit = False

while quit != True:
    option = input ("Homework 5 Menu\n1-Hamming Distance\n2-Dna Complement\n3-Exit")
    option = int(option)

    while option == 1:
        dna1 = input ("Enter a DNA string made up of A, T, C, and G proteins.")
        dna1 = str(dna1)
        dna2 = input ("Enter a DNA string made up of A, T, C, and G proteins the same length as the previous string.")
        dna2 = str(dna2)
        if len(dna1) == len(dna2):
            ham = strings.get_hamming_distance(dna1, dna2)
            print(ham)
            exit = input ("Do you want to exit>\n1 - Yes\n2 - no")
            exit = int(exit)
            if exit == 1:
                exit = 0
                option = 0
                print("Goodbye")
                quit = True
            elif exit == 2:
                exit = 0
                option = 0
        else:
            print ("Strings are not of equal length.")
            
    while option == 2:
        dna1 = input ("Enter a DNA string made up of A, T, C, and G proteins.")
        dna1 = str(dna1)
        com = strings.get_dna_complement(dna1)
        print(com)
        exit = input ("Do you want to exit>\n1 - Yes\n2 - no")
        exit = int(exit)
        if exit == 1:
            exit = 0
            option = 0
            print("Goodbye")
            quit = True
        elif exit == 2:
            exit = 0
            option = 0     
    while option == 3:
        exit = input ("Are you sure you want to exit?\n1 - Yes\n2 - No")
        exit = int(exit)
        if exit == 1:
            exit = 0
            option = 0
            print("Goodbye")
            quit = True
        elif exit == 2:
            exit = 0
            option = 0
