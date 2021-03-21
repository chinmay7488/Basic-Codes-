from PIL import Image, ImageDraw, ImageFont
#import ttfquery.findsystem 
import string
import ntpath
import numpy as np
import os
import glob
 
fontSize = 60
imgSize = (128,128)
position = (0,0)
 
#All images will be stored in 'Synthetic_dataset' directory under current directory
dataset_path = os.path.join (r'D:\Chinmay Jain\Subject\Projects\Font Creater', 'Synthetic_dataset')
if not os.path.exists(dataset_path):
   os.makedirs(dataset_path)
 
fhandle = open(r'D:\Chinmay Jain\Subject\Projects\Font Creater\Fonts_list.txt', 'r')
lower_case_list = list(string.ascii_lowercase)
upper_case_list = list(string.ascii_uppercase)
digits = range(0,10)
 
digits_list=[]
for d in digits:
   digits_list.append(str(d))
 
all_char_list = lower_case_list + upper_case_list + digits_list
 
fonts_list = []
for line in fhandle:
   fonts_list.append(line.rstrip('\n'))
 
total_fonts = len(fonts_list)
#paths = ttfquery.findsystem.findFonts()
all_fonts = glob.glob("C:\\Windows\\Fonts\\*.ttf")
f_flag = np.zeros(total_fonts)
 
for sys_font in all_fonts:
   #print "Checking "+p
   font_file = ntpath.basename(sys_font)
   font_file = font_file.rsplit('.')
   font_file = font_file[0]
   f_idx = 0
   for font in fonts_list:
      f_lower = font.lower()
      s_lower = sys_font.lower()
      #Check desired font
      if f_lower in s_lower:
         path = sys_font
         font = ImageFont.truetype(path, fontSize)
         f_flag[f_idx] = 1
         for ch in all_char_list:
            image = Image.new("RGB", imgSize, (255,255,255))
            draw = ImageDraw.Draw(image)
            pos_x = 54
            pos_y = 30
            pos_idx=0
            for y in [pos_y-1, pos_y, pos_y+1]:
               for x in [pos_x-1, pos_x, pos_x+1]:
                  position = (x,y)
                  draw.text(position, ch, (0,0,0), font=font)
                  ##without this flag, it creates 'Calibri_a.jpg' even for 'Calibri_A.jpg'
                  ##which overwrites lowercase images
                  l_u_d_flag = "u"
                  if ch.islower():
                     l_u_d_flag = "l"
                  elif ch.isdigit():
                     l_u_d_flag = "d"
                  file_name1 = os.path.join(dataset_path,ch)
                  if not os.path.exists(file_name1):
                     os.makedirs(file_name1)
                  file_name2 = os.path.join(file_name1,l_u_d_flag)
                  if not os.path.exists(file_name2):
                     os.makedirs(file_name2)
                  file_name = font_file+'_'+l_u_d_flag+'_'+ch + '.jpg'
                  file_name = os.path.join(file_name2, file_name)
                  image.save(file_name)
                  pos_idx = pos_idx + 1
      f_idx = f_idx + 1
 
