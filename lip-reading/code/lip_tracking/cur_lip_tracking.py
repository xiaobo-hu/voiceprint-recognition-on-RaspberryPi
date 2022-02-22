import numpy as np
import cv2
import dlib
import argparse

import face_utils

# step 1: set arguments
"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", default="../../data/sample_video.mp4",
                help="path to input video file")
ap.add_argument("-o", "--output",
                help="path to output video file")
ap.add_argument("-f", "--fps", type=int, default=30,
                help="FPS of output video")
ap.add_argument("-c", "--codec", type=str, default="MJPG",
                help="codec of output video")
args = vars(ap.parse_args())
"""

# step 2: Dlib requirements
# 可更改路径
shape_detector_path = '../../model/dlib/shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_detector_path)
# 取dlib与嘴唇有关的点数（起点-终点）
MOUSE_START = 49 - 1
MOUSE_END = 68 - 1

# step 3: 创建VideoCapture，传入0即打开系统默认摄像头
# 由于调试，本处通过本地的参数输入
cap = cv2.VideoCapture(0) # args["input"])

# step 4: 开始检测
while True:
    ret, frame = cap.read()  # ret为bool类型，指示是否成功读取这一帧
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 处理一帧，转为灰度图

    # 返回值是<class 'dlib.dlib.rectangle'>，就是一个矩形
    # 坐标为[(x1, y1) (x2, y2)]
    rets = detector(gray, 1)

    for ret in rets:
        shape = predictor(gray, ret)
        points = face_utils.shape_to_np(shape)
        mouse_points = points[MOUSE_START:MOUSE_END]

        # 使用cv2.convexHull获得位置的凸包位置
        mouseHull = cv2.convexHull(mouse_points)
        (x, y, w, h) = cv2.boundingRect(mouseHull)

        # 画出矩形 (0,255,9)是画线对应的rgb颜色、2是所画的线的宽度
        # border = 5
        # cv2.rectangle(frame, (x - border, y - border), (x + w + border, y + h + border), (0, 255, 9), 2)
        # 使用cv2.drawContours画出轮廓图
        cv2.drawContours(frame, [mouseHull], -1, (0, 255, 0), 1)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC退出
        break
    cv2.imshow("Frame", frame)

# step 5: release
cap.release()
cv2.destroyAllWindows()
