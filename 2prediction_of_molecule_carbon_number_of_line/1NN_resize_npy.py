import os.path
import cv2
import matplotlib.pyplot as plt
import copy
import numpy as np

"""
# 指定要查詢的路徑
yourPath = r'D:/New/molecule_avo_fig/4/20/400X55555555/400all'  # 檔名不能是中文，會出錯
# 列出指定路徑底下所有檔案(包含資料夾)
allFileList = os.listdir(yourPath)
# 逐一查詢檔案清單
a = 0
l = int(input('編號'))
data = []
for file in allFileList:
    # print(file)
    im = cv2.imread(yourPath + '//' + str(file))  # , cv2.IMREAD_GRAYSCALE 輸入是圖是array就不用轉
    # print(im.shape)
    dst = cv2.resize(im, (300, 300), interpolation=cv2.INTER_AREA)  # https://blog.csdn.net/guyuealian/article/details/85097633
    # plt.imshow(dst)
    # plt.show()
    # print(type(dst))
    data.append([dst, l])  # https://mathpretty.com/11796.html
    a += 1

    
    if a==1:
        break

#  02:0\04:1\06:2\08:3\10:4\12:5\14:6\16:7\18:8\20:9
# print(data)
img = np.array([i[0] for i in data])
label = np.array([i[1] for i in data])
print(img.shape, label.shape)
print(img[0:2])
np.save('20C_' + str(l) + '_img', img)
np.save('20C_' + str(l) + '_label', label)
"""

yourPath = r'D:/New/molecule_avo_fig/ring/1/1200X300X300/no_resize/5C/all'
allFileList = os.listdir(yourPath)
l = int(input('編號'))
data = []
for file in allFileList:
    # print(file)
    im = cv2.imread(yourPath + '//' + str(file))  # , cv2.IMREAD_GRAYSCALE 輸入是圖是array就不用轉
    # print(im.shape)
    dst = cv2.resize(im, (300, 300), interpolation=cv2.INTER_AREA)  # https://blog.csdn.net/guyuealian/article/details/85097633
    # plt.imshow(dst)
    # plt.show()
    # print(type(dst))
    # dst = dst/255
    data.append([dst, l])  # https://mathpretty.com/11796.html
# 值鏈編號:0，環編號:1
img = np.array([i[0] for i in data])
label = np.array([i[1] for i in data])
print(img.shape, label.shape)
print(img[0:2])
np.save('5C' + str(l) + '_img', img)
np.save('5C' + str(l) + '_label', label)

