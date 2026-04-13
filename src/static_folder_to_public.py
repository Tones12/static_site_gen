import os
import shutil


def static_folder_to_public_folder():
    public_path = 'docs'
    static_path = 'static'

    if not os.path.exists(static_path):
        raise Exception("static folder does not exist")

    # Remove Public and create clean directory
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
        os.makedirs(public_path)
    else:
        os.makedirs(public_path)

    # recursively copy and paste to public directory
    directory_and_file_list = os.listdir(static_path)
    for item in directory_and_file_list:
        path = os.path.join(static_path, item)
        copy_paste_item(path, public_path)

def copy_paste_item(item_path, destination_path):
    if os.path.isfile(item_path):
        shutil.copy(item_path, destination_path)
        print(f"Copied {item_path} to {destination_path}")
    else:
        new_directory = os.path.join(destination_path, os.path.basename(item_path))
        os.makedirs(new_directory)
        print(f"Created directory {os.path.basename(item_path)} in {destination_path}")
       
        for item in os.listdir(item_path):
            new_path = os.path.join(item_path, item)
            copy_paste_item(new_path, new_directory)






    
        
    




    
