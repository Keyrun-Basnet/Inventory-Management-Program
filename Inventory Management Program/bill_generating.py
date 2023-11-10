import file_write
import datetime
import operations

date_ = datetime.datetime.now()

# rent and return bill generating------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bill_rent(name, contact, total_price):

    file_write.file_write_rent(name, contact, total_price)

    #displaying bill
    print()   
    print('----------------------------------------------------------')
    print("                     Bill Details.")
    print('----------------------------------------------------------')
    print()
    print("Name of the Customer :","\t",name)
    print("Contact information :","\t",contact)
    print("Date of renting :","\t",date_.strftime("%c"))
    print()
    print('----------------------------------------------------------')
    print()
    print("Your rented costumes are :")
    for each in operations.cart_rent:
        print(each)
    print()
    print('----------------------------------------------------------')
    print("Total price :","\t","\t","$",total_price)
    print('----------------------------------------------------------')
    print()
    print()
    

def bill_return(name, contact, total_fine):

    file_write.file_write_return(name, contact, total_fine)
    
    #displaying bill
    print('----------------------------------------------------------')
    print("                     Bill Details.")
    print('----------------------------------------------------------')
    print()
    print("Name of the Customer :","\t",name)
    print("Contact information :","\t",contact)
    print("Date of renting :","\t",date_.strftime("%c"))
    print()
    print('----------------------------------------------------------')
    print()
    print("Your renturned costumes are :")
    for each in operations.cart_return:
        print(each)
    print()
    print('----------------------------------------------------------')
    print("Total fine :","\t","\t","$",total_fine)
    print('----------------------------------------------------------')
    print()
    print()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
