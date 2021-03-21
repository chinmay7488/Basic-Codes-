import os 
#path = r'D:\Chinmay Jain\Subject\Projects\OCR task\dataset\OCR_Handwritten_dataset for Forms'
DIRECTORY = r"D:\Chinmay Jain\Subject\Projects\OCR task\dataset\OCR_Handwritten_dataset for Forms"
CATEGORIES = os.listdir(DIRECTORY)
#print(CATEGORIES)
data=[]
labels=[]
for category in CATEGORIES:
    path = os.path.join(DIRECTORY, category)
    for img in os.listdir(path):
    	img_path = os.path.join(path, img)
        data.append(img_path)
    	labels.append(category)
print(data)
