import os
import shutil

def move_jpg_files(source_folder,destination_folder):
    if not os.path.exists(source_folder):
        print("Source Folder does not exist.")
        return
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".jpg"):
            source_path=os.path.join(source_folder,file_name)
            destination_path=os.path.join(destination_folder,file_name)    
            shutil.move(source_path,destination_path)
            print(f"Moved : {file_name}")
            print("\nAll .jpg files have been moved successfully!")

source="C:\\Users\\Public"            
destination="C:\\Users\\daast"
move_jpg_files(source,destination)