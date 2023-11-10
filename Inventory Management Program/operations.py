import datetime
import dictionary
import file_write
import valid_input
import bill_generating

cart_rent = []
cart_return = []

date_ = datetime.datetime.now()
year = str(datetime.datetime.now().year)
minute = str(datetime.datetime.now().month)
second = str(datetime.datetime.now().second)




# head, menu and costume list------------------------------------------------------------------------------------------------------------------------------------------------------------

#header_ function
def header_():
    print()
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('             Welcome to Costume Rental Store.')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print()


#menu_ function
def menu_():
    print("select a desirable option :")
    print()
    print("(1) || Press 1 to rent a costume.")
    print("(2) || Press 2 to return a costume.")
    print("(3) || Press 3 to exit.")


#print custome list
def print_costume():
    file_content = dictionary.get_file_content()
    main_data = dictionary.get_dictionary(file_content)

    print('----------------------------------------------------------')
    print("ID","\t","Costume Name","\t"," Brand","\t","Price","\t","Quantity")
    print('----------------------------------------------------------')
    
    for key, value in main_data.items():
        print(key,"\t",value[0],"\t",value[1],"\t",value[2],"\t",value[3])
    print('----------------------------------------------------------')
    print()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# input options -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#option 1
def option_1():
    print()
    print("Lets rent a costume.")
    print()

    price = 0
    total_price = 0
    Loop = True
    while Loop == True:
        
        print_costume() #print custome list

        file_content = dictionary.get_file_content()
        main_data = dictionary.get_dictionary(file_content)
        ID = valid_input.get_valid_ID()
        quantity = valid_input.get_rent_quantity(ID)
        cart_rent.append ([ID,main_data[ID][0],main_data[ID][2],quantity])

        #change quantity in the file
        file_content = dictionary.get_file_content()
        main_data = dictionary.get_dictionary(file_content)            
            
        main_data[ID][3] = str(int(main_data[ID][3]) - quantity)
        file = open("costume.txt","w")
        for value in main_data.values():
            write_data = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
            file.write(write_data)
        file.close()

        #calculating price
        price = int(main_data[ID][2].replace("$",""))*quantity
        total_price += price

        nextInput = input("Do you want to rent more costumes ? (y/n) ")

        if nextInput == "n":
            print()
            name = input("Enter the customer's Name :")
            print()
            contact = input("Enter the customer's Contact :")
            print()
            
            bill_generating.bill_rent(name, contact, total_price)
            
            print('----------------------------------------------------------')
            print("     You have successfully rented the custome/s.")
            print('----------------------------------------------------------')
            Loop = False

#option 2
def option_2():
    print()
    print("Lets return a costume.")
    print()

    total_days = 0
    total_quantity =0
    fine_ = 0.25
    Loop = True
    while Loop == True:
        x = True
        while x == True:
        
            print_costume() #print custome list

            file_content = dictionary.get_file_content()
            main_data = dictionary.get_dictionary(file_content)
            ID = valid_input.get_valid_ID()
            quantity = valid_input.get_return_quantity(ID)
            cart_return.append ([ID,main_data[ID][0],main_data[ID][2],quantity])
            
            #change quantity in the file
            file_content = dictionary.get_file_content()
            main_data = dictionary.get_dictionary(file_content)            
                
            main_data[ID][3] = str(int(main_data[ID][3]) + quantity)
            file = open("costume.txt","w")
            for value in main_data.values():
                write_data = value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
                file.write(write_data)
            file.close()

            #calculating fine
            print()
            rented_days = int(input("How many days since you have rented the customes :"))
            print()
            if rented_days > 5:
                total_days += (rented_days - 5)
                total_quantity += quantity 
                total_fine = total_days * total_quantity *fine_
            else:
                total_fine = 0
            print()
            nextInput = input("Do you want to return more customes ? (y/n) ")
            print()
            x = False
            
        if nextInput == "n":
            name = input("Enter the customer's Name :")
            print()
            contact = input("Enter the customer's Contact :")
            
            bill_generating.bill_return(name, contact, total_fine)
            
            print()
            print('----------------------------------------------------------')
            print("     You have successfully returned the custome/s.")
            print('----------------------------------------------------------')
            Loop = False

#option 4
def option_3():
    print()
    print("Thank you for using the software.")
    print()

#invalid option
def invalid_option():
    print()
    print('----------------------------------------------------------')
    print("                    invalid option.")
    print("                  Enter valid number.")
    print('----------------------------------------------------------')
    print()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




