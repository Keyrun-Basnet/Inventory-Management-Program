import dictionary
import datetime
import operations

date_ = datetime.datetime.now()
year = str(datetime.datetime.now().year)
minute = str(datetime.datetime.now().month)
second = str(datetime.datetime.now().second)

# creating bill for rent and return --------------------------------------------------------------------------------------------------------------------------------------------------------

#file creation for bill_rent
def file_write_rent(name, contact, total_price):
    file_content = dictionary.get_file_content()
    main_data = dictionary.get_dictionary(file_content)
    price_rent = str(total_price)
    
    file = open(name+"_"+year+minute+second+".txt","w")
    file.write('++++++++++++++++++++++++++++++++++++++++++++++++'+"\n")
    file.write("                   Rent Bill Details."+"\n")
    file.write('++++++++++++++++++++++++++++++++++++++++++++++++'+"\n")
    file.write("\n")
    file.write("Name of the Customer :"+name+"\n")
    file.write("Contact information :"+contact+"\n")
    file.write("Date of renting :"+date_.strftime("%c")+"\n")
    file.write("\n")
    file.write("------------------------------------------------"+"\n")
    file.write("S.No"+"\t"+"Costume Name"+"\t"+" Brand"+"\t"+"Price"+"\t"+"Quantity"+"\n")
    file.write("------------------------------------------------"+"\n")
    file.write("\n")
    for index in range(len(operations.cart_rent)):
        c_sno = int(operations.cart_rent[index][0])
        c_quantity = int(operations.cart_rent[index][3])
        c_name = main_data[c_sno][0]
        c_brand = main_data[c_sno][1]
        c_price = int(main_data[c_sno][2].replace("$","")) * c_quantity
        file.write(str(index+1)+"\t"+c_name+"\t"+c_brand+"\t"+str(c_price)+"\t"+str(c_quantity))
        file.write('\n')
    file.write("\n")
    file.write("------------------------------------------------"+"\n")
    file.write("Total price : $"+price_rent+"\n")
    file.write("------------------------------------------------"+"\n")
    file.close()

#file creation for bill_return
def file_write_return(name, contact, total_fine):
    file_content = dictionary.get_file_content()
    main_data = dictionary.get_dictionary(file_content)
    price_return = str(total_fine)
    
    file = open(name+"_"+year+minute+second+".txt","w")
    file.write('++++++++++++++++++++++++++++++++++++++++++++++++'+"\n")
    file.write("                 Return Bill Details."+"\n")
    file.write('++++++++++++++++++++++++++++++++++++++++++++++++'+"\n")
    file.write("\n")
    file.write("Name of the Customer :"+name+"\n")
    file.write("Contact information :"+contact+"\n")
    file.write("Date of renting :"+date_.strftime("%c")+"\n")
    file.write("\n")
    file.write("------------------------------------------------"+"\n")
    file.write("S.No"+"\t"+"Costume Name"+"\t"+" Brand"+"\t"+"Price"+"\t"+"Quantity"+"\n")
    file.write("------------------------------------------------"+"\n")
    file.write("\n")
    for index in range(len(operations.cart_return)):
        c_sno = int(operations.cart_return[index][0])
        c_quantity = int(operations.cart_return[index][3])
        c_name = main_data[c_sno][0]
        c_brand = main_data[c_sno][1]
        c_price = int(main_data[c_sno][2].replace("$","")) * c_quantity
        file.write(str(index+1)+"\t"+c_name+"\t"+c_brand+"\t"+str(c_price)+"\t"+str(c_quantity))
        file.write('\n')
    file.write("\n")    
    file.write("+------------------------------------------------"+"\n")
    file.write("Total fine : $"+price_return+"\n")
    file.write("------------------------------------------------"+"\n")
    file.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
