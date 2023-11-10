import operations
  
# main ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

continueLoop = True
while continueLoop == True:

    operations.header_()
    
    operations.menu_()

    #For inputing options
    print()
    x = input("Enter a option :")

    #when input is 1.
    if x == '1':
        operations.option_1()
        
    #when input is 2.
    elif x == '2':
        operations.option_2()

    #when input is 3.
    elif x == '3':
        operations.option_3()
        continueLoop = False

    #when input is not valid
    else:
        operations.invalid_option()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
