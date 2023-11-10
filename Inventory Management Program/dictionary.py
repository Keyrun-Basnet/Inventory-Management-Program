
# creating file_content and data_dictionary----------------------------------------------------------------------------------------------------------------------------------------------

#read file function
def get_file_content():
    file = open("costume.txt","r")
    data = file.readlines()
    file.close()
    return data


#get dictionary
def get_dictionary(file_content):
    data_dictionary = {}
    for index in range(len(file_content)):
        data_dictionary[index + 1] = file_content[index].replace("\n","").split(",")
    return data_dictionary

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
