
import os
import shutil
root_path=input("Enter the root path: ")
file_modules={
"Images":[".jpg",".jpeg",".png",".gif",".bmp"],
"Documents":[".pdf",".doc",".docx",".txt"],
"Audio":[".mp3"],
"Videos":[".mp4",".avi",".mov"],
"Compressed Files":[".zip","rar",".7z"]

}

for modules in file_modules:
        os.makedirs(os.path.join(root_path,modules),exist_ok=True)

miscellanious_folder=os.path.join(root_path,"others")
os.makedirs(miscellanious_folder,exist_ok=True)

for file in os.listdir(root_path):
        path=os.path.join(root_path,file)

        if os.path.isfile(path):

            organized=False
            for modules,extension in file_modules.items():
                if file.lower().endswith(tuple(extension)):
                    shutil.move(os.path.join(root_path,file),os.path.join(root_path,modules,file))
                    organized=True
                    break
            if not organized:

                    if not os.path.exists(miscellanious_folder):
                        os.makedirs(miscellanious_folder,exists=True)
                    shutil.move(os.path.join(path,file),os.path.join(miscellanious_folder,file))
print("Finished Successfully Organized Files")


