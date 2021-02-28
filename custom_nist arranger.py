import shutil
import os

move_folder = ['hsf_0','hsf_1','hsf_2','hsf_3','hsf_4','hsf_6','hsf_7','train_79']
delete_file = {'hsf_0.mit','hsf_1.mit','hsf_2.mit','hsf_3.mit','hsf_4.mit','hsf_6.mit','hsf_7.mit'}
path = r'D:\Chinmay Jain\Subject\Datasets\NIST\by_class'
f = os.listdir(path)
for f1 in f:
    move_folder[7] = "train_"+f1
    source_dir = os.path.join(path,f1)
# source_dir = r'D:\Chinmay Jain\Subject\Projects\OCR_Handwritten_Custom\Data\NIST\by_class\79'
# target_dir = r'D:\Chinmay Jain\Subject\Projects\OCR_Handwritten_Custom\Data\NIST\by_class\79'

    for i in move_folder:    
        folder_names = os.path.join(source_dir, i)
        if os.path.exists(folder_names) == True:
            if os.listdir(folder_names) != None:
                if os.listdir(folder_names) != None:
                    files = os.listdir(folder_names)
                    for file_name in files:
                        shutil.move(os.path.join(folder_names, file_name), source_dir)
                else:    
                    shutil.rmtree(folder_names)
            shutil.rmtree(folder_names)

    for j in delete_file:
        n = os.path.join(source_dir, j)
        if os.path.isfile(n):
            os.remove(n)