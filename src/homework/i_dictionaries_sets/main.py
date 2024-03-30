import dictionary

option = 0
quit = False
widgets = {}

while quit == False:
    option = input("Homework 6 Menu\n1-Add or Update Item\n2-Delete Item\n3-Exit")
    option = int(option)

    while option == 1:
        widget_name = input("Enter item name")
        quantity = input ("Enter item quantity. Enter negative to subtract.")
        quantity = int(quantity)
        dictionary.add_inventory(widgets, widget_name, quantity)
        print (widgets) #used to check the dictionary after each menu choice
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
        widget_name = input("Enter item name")
        delete = dictionary.remove_inventory_widget (widgets, widget_name)
        print (delete)
        print (widgets)
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
