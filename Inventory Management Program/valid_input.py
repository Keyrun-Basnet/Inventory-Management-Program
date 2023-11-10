import dictionary

# for getting valid ID, rent quantity and return quantity-------------------------------------------------------------------------------------------------------------------------------- 

#getting valid input for ID
def get_valid_ID():
    file_content = dictionary.get_file_content()
    main_data = dictionary.get_dictionary(file_content)
    valid_input = False
    
    while valid_input == False:
        try:
            ID = int(input("Enter the ID of the costume you want to rent/return :"))
            if ID > 0 and ID <= len(main_data):
                valid_input = True
                print()
                print('----------------------------------------------------------')
                print("                 Costume is available.")
                print('----------------------------------------------------------')
                print()
            else:
                print()
                print('----------------------------------------------------------')
                print("               Invalid ID. Try again.")
                print('----------------------------------------------------------')
                print()
        except:
            print()
            print('----------------------------------------------------------')
            print("               Invalid ID. Try again.")
            print('----------------------------------------------------------')
            print()
    return ID


#getting valid input for rent quantity
def get_rent_quantity(ID):
    file_content = dictionary.get_file_content()
    main_data = dictionary.get_dictionary(file_content)
    quantity = main_data[ID][3]
    quantity = int(quantity)
    
    valid_input = False
    while valid_input == False:
        try:
            input_quantity = int(input("Enter Quantity of costume :"))
            if input_quantity > 0 and input_quantity <= quantity:
                valid_input = True
                print()
                print('----------------------------------------------------------')
                print("                  Stock is available.")
                print('----------------------------------------------------------')
                print()
            elif(input_quantity == 0):
                print()
                print('----------------------------------------------------------')
                print("                     Invalid input.")
                print('----------------------------------------------------------')
                print()
            else:
                print()
                print('----------------------------------------------------------')
                print("                   Not Enough Stock.")
                print('----------------------------------------------------------')
                print()
        except:
            print()
            print('----------------------------------------------------------')
            print("                     Invalid input.")
            print('----------------------------------------------------------')
            print()
    return input_quantity


#getting valid input for return qunatity
def get_return_quantity(ID):
    file_content = dictionary.get_file_content()
    main_data = dictionary.get_dictionary(file_content)
    quantity = main_data[ID][3]
    quantity = int(quantity)
    
    valid_input = False
    while valid_input == False:
        try:
            input_quantity = int(input("Enter Quantity of costume :"))
            if input_quantity > 0:
                valid_input = True
            else:
                print()
                print('----------------------------------------------------------')
                print("                     Invalid input.")
                print('----------------------------------------------------------')
                print()
        except:
            print()
            print('----------------------------------------------------------')
            print("                     Invalid input.")
            print('----------------------------------------------------------')
            print()
    return input_quantity

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
