''' OBJECT PROCESSOR'''

import glob
import shutil
import zipfile
from zipfile import ZipFile
import os

##### Directing paths ######
source_path = '../Source/*'
curr_path = os.getcwd()
Destination_path = '../Destination'


##### Directing Source paths object & copy in server ######
source_obj = glob.glob(source_path)
for source_obj_items in range(len(source_obj)):
        obj_path = source_obj[source_obj_items]
        

        obj_name = obj_path.split('\\')[-1].split('.')
        prefix = obj_name[0]
        postfix = obj_name[1]


        ############ checking is it text file ############
        if postfix=='txt':
            shutil.copy(obj_path, '.') 
            ##### Renaming the server files & writting the lines ######
            with open(obj_path, 'r') as file:
                lines = file.readlines()

            fileList = []
            for item in range(1, 4):
                filename = f'{prefix}_{item}.{postfix}'
                with open(filename, 'w') as file:
                    for file_line in range(item*10):
                        file.write(lines[file_line])
                fileList.append(filename)
                print(filename)



            ##### zipping the files & sending in Destination #####
            filename = f'{prefix}.zip'
            with zipfile.ZipFile(filename, 'w', compression=zipfile.ZIP_DEFLATED) as make_zip:
                for files in fileList:
                    make_zip.write(files)
            make_zip.close()
            shutil.move(f'{curr_path}\{filename}', f'{Destination_path}/{filename}')


            ##### unzip files folder from destination #####
            DesfilePath = '../Destination/*'
            DesfilePath_obj = glob.glob(DesfilePath)

            name = prefix
            with zipfile.ZipFile(DesfilePath_obj[0], 'r') as make_zip:
                make_zip.extractall(name)
            make_zip.close()
            shutil.move(f'{curr_path}\{name}', f'{Destination_path}/{name}')


            ######### removing the files ############
            os.remove(obj_path.split('\\')[-1])     # removed some.txt server file
            cur_dir_list = os.listdir(os.getcwd())

            for curDirList_items in cur_dir_list:
                curDirList_items_name = curDirList_items.split('.')
                postfix2 = curDirList_items_name[1]
                if postfix2 == 'txt':
                    os.remove(curDirList_items)
            
        
        
        ############ checking is it py file ############
        if postfix == 'py':
            try:
                exec(open(obj_path).read())
            except:
                print('An ERROR has been Occured')
    

    



