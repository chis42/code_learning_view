import cv2
import os

video_path = 'C:/Users/biersaa/Desktop/VideoCut/wuhu.mp4'  # 视频文件地址，是视频文件
timeF = 1  # 隔timeF帧截一次图，1表示全截


images_path = video_path.split('.', 1)[0]
if not os.path.exists(images_path):  # 文件夹不存在则新建
    os.mkdir(images_path)

vc = cv2.VideoCapture(video_path) # 读入视频文件
c = 1
rat = 1
if vc.isOpened(): # 判断是否正常打开
    print('视频读取成功，正在逐帧截取...')
    while rat:  # 循环读取视频帧
        rat, frame = vc.read()  # frame为一帧图像，当frame为空时，ret返回false，否则为true
        if(c%timeF == 0 and rat == True): # 每隔timeF帧截一次图像
            cv2.imwrite(images_path + '/' +  str(c) + '.jpg',frame)
        c = c + 1
    vc.release()
    print('截取完成，图像保存在：%s' %images_path)
else:
    print('视频读取失败，请检查文件地址')
