import matplotlib.pyplot as plt
import cv2
from moviepy.editor import VideoFileClip
import os
import numpy as np
import copy

def cutvideotoimage(inputname,outputname,foldernamed,imgnumber):
  clip = VideoFileClip(inputname)
  print( clip.duration ) # seconds
  vidcap = cv2.VideoCapture(inputname)
  if not os.path.exists(foldernamed):
    os.makedirs(foldernamed)
  else:
    import shutil
    shutil.rmtree(foldernamed)
    os.makedirs(foldernamed)
  def getFrame(sec):
      vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
      hasFrames,image = vidcap.read()
      if hasFrames:
          cv2.imwrite(foldernamed+'/'+outputname+str(count)+".png", image)     # save frame as JPG file
      return hasFrames
  sec = 0
  frameRate = clip.duration/imgnumber #//it will capture image in each 0.5 second
  #print(imgnumber)
  count=1
  success = getFrame(sec)
  while success:
      count = count + 1
      sec = sec + frameRate
      sec = round(sec, 2)
      success = getFrame(sec)
  yourPath = r''+foldernamed
  allFileList = os.listdir(yourPath)
  d=[]
  for file in allFileList:
    im = copy.deepcopy(cv2.imread(yourPath + '//'+str(file)))
    dst = cv2.resize(im, (300,300), interpolation=cv2.INTER_AREA)
    d.append([dst])
  img = np.array([i[0] for i in d])
  #plt.figure()
  #for i in range(1,10):  # https://blog.csdn.net/qwe2508/article/details/88078746
    #plt.subplot(5,2,i)
    #plt.imshow(img[i-1])
  #plt.show()
  return img

#直鏈
"""
straightnumber=3000
yourPath = r'D:/New/molecule_avo_fig/4/oCam'  # 檔名不能是中文，會出錯
# 列出指定路徑底下所有檔案(包含資料夾)
allFileList = os.listdir(yourPath)
# 逐一查詢檔案清單
a=0
l = int(input('編號'))
data=[]
for file in allFileList:
    yourPath2 = r'D:/New/molecule_avo_fig/4/oCam'+'/'+file
    allFileList2 = os.listdir(yourPath2)
    for file2 in allFileList2:
        print(len(allFileList2),'4')
        yourPath3 = r'D:/New/molecule_avo_fig/4/oCam' +'/'+ file+'/'+file2
        allFileList3 = os.listdir(yourPath3)
        for file3 in allFileList3:
            #print(file3)
            inputnamemp4='D:/New/molecule_avo_fig/4/oCam' +'/'+ file+'/'+file2+'/'+file3
            foldername='D:/New/molecule_avo_fig/predict_ringorstraight' +'/'+ file
            if os.path.exists(foldername):
                print("路徑存在。")
            else:
                print("路徑不存在。")
                os.makedirs(foldername)
            foldernamed = 'D:/New/molecule_avo_fig/predict_ringorstraight' + '/' + file+'/'+file2
            if os.path.exists(foldernamed):
                print("路徑存在。")
            else:
                print("路徑不存在。")
                os.makedirs(foldernamed)
            imgnumber=int((straightnumber/10)/(len(allFileList2)*3))+5
            print(imgnumber)
            foldernamed3 = 'D:/New/molecule_avo_fig/predict_ringorstraight' + '/' + file + '/' + file2+ '/' + file3[:-4]
            cutvideotoimage(inputnamemp4, file2+file3[:-4], foldernamed3,imgnumber)
"""

ringnumber=2400
yourPath = r'D:/New/molecule_avo_fig/ring/1/oCam/6C'  # 檔名不能是中文，會出錯
# 列出指定路徑底下所有檔案(包含資料夾)
allFileList = os.listdir(yourPath)
# 逐一查詢檔案清單
a=0
#l = int(input('編號'))
data=[]
for file in allFileList:
            inputnamemp4='D:/New/molecule_avo_fig/ring/1/oCam/6C/'+ file
            foldername='D:/New/molecule_avo_fig/ring/1/1200X300X300/no_resize/6C/'+ file[:-4]
            if os.path.exists(foldername):
                print("路徑存在。")
            else:
                print("路徑不存在。")
                os.makedirs(foldername)
            imgnumber=int((ringnumber/2)/3)+200
            print(imgnumber)
            cutvideotoimage(inputnamemp4, '5C'+file[:-4], foldername,imgnumber)


