import os, random
import shutil

folder = os.listdir(r'D:\Chinmay Jain\Subject\Datasets\custom_OCR_Train\Train')
for i in folder:
    path = os.path.join(r"D:\Chinmay Jain\Subject\Datasets\custom_OCR_Train\Train", i)

    out_dir = os.path.join(r"D:\Chinmay Jain\Subject\Datasets\custom_OCR_Train\Valid", i)

    if os.path.isdir(out_dir) == False:
        os.makedirs(out_dir)

    for i in range(0, 5210):
        files = os.listdir(path)
        file_name = random.choice(files)
        shutil.move(os.path.join(path, file_name), out_dir)
