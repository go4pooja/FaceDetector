import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from os.path import join
import xlsxwriter as sexy
def detectF(cascade, test_image, scaleFactor = 1.3):
    img = test_image.copy()
    test_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(test_gray, scaleFactor = scaleFactor, minNeighbors = 5)
    return len(faces)


cassy = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#q = detectF(cassy, cv2.imread('data/baby1.png'))
#print(q)
i = 0
image_list = list()
image_dir = 'china_male_53/'
with os.scandir('china_male_53/') as root_dir:
    for path in root_dir:
        if path.is_file():
            i += 1
            #print(f"Full path is: {path} and just the name is: {path.name}")
            image_list.append(join(image_dir,path.name))
print(f"{i} files scanned successfully.")
#print(image_list)
def get_res(image_lists):
    dic = dict()
    for i in image_list:
        dic[i] = detectF(cassy, cv2.imread(i))
    return dic
result = get_res(image_list)
workbook = sexy.Workbook('image&face_3_5.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0,'Images')
worksheet.write(0,1,'Faces')
row = 1
col = 0
#sorted(result.items())

for k,v in result.items():
    worksheet.write(row,col,k)
    worksheet.write(row,col+1,v)
    row = row+1
workbook.close()
print('done')
