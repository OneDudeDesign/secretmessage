import os

def rename_files():
    # (1) get file names from the directory
    file_list = os.listdir(r'/Users/clucier/Desktop/ODD/Udacity/pf-python/secretmessage/encodedphotos/prank')

    print file_list

# rename the files

rename_files()
