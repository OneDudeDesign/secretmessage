import os
file_directory = r'/Users/clucier/Desktop/ODD/Udacity/pf-python/secretmessage/encodedphotos/prank'
def rename_files():


    # (1) get file names from the directory
    file_list = os.listdir(file_directory)

    print file_list

    # rename the files
    saved_path = os.getcwd()
    os.chdir(file_directory)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0,1,2,3,4,5,6,7,8,9"))
    os.chdir(saved_path)

    # check new list
    new_file_list = os.listdir(file_directory)
    print new_file_list

rename_files()
