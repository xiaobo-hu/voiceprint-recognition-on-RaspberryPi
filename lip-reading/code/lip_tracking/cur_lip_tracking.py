import numpy as np
import time


def feature_standardization(feature):
    feature -= feature[0, :]  # 以point48作为基准定位
    mean_each_col = np.average(feature, axis=0)

    # 总体方差
    variance_each_col = np.sqrt(np.sum((feature - mean_each_col) ** 2, axis=0) / feature.shape[0])
    # 样本方差
    # variance_each_col = np.sqrt(np.sum((feature - mean_each_col) ** 2,axis = 0) / (feature.shape[0] - 1))

    ret = (feature - mean_each_col) / variance_each_col
    return ret


def euclidean_distance(x, y):
    return np.sum((x - y) ** 2)


def lip_tracking():
    import cv2
    import dlib

    import face_utils

    # step 1: set arguments
    import sys, os
    pwd = sys.path[0]
    father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")

    face_predictor_path = os.path.join(father_path, "model/dlib/shape_predictor_68_face_landmarks.dat")
    # test_video_path = os.path.join(father_path, "data/move.mp4")

    # step 2: Dlib requirements
    shape_detector_path = face_predictor_path
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(shape_detector_path)
    # 取dlib与嘴唇有关的点数（起点-终点）
    MOUSE_START = 48
    MOUSE_END = 68
    font = cv2.FONT_HERSHEY_SIMPLEX

    # step 3: 创建VideoCapture，传入0即打开系统默认摄像头
    # 由于调试，本处通过本地的参数输入
    # cap = cv2.VideoCapture(test_video_path)  # cv2.VideoCapture(0) # args["input"])
    cap = cv2.VideoCapture(0)
    cap.set(6, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))

    points_recorder_last, points_recorder_now = np.zeros((20, 2)), np.zeros((20, 2))
    cnt = 0

    # step 4: 开始检测
    run_time = 3
    total_count, moving_count = 0, 0
    FPS = 30
    total_frame = FPS * run_time
    count_frame = 0

    print("start recording pictures..")
    while count_frame <= total_frame:

        count_frame += 1

        ret, frame = cap.read()  # ret为bool类型，指示是否成功读取这一帧

        if not count_frame % 4:

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 处理一帧，转为灰度图
            # 返回值是<class 'dlib.dlib.rectangle'>，就是一个矩形
            # 坐标为[(x1, y1) (x2, y2)]
            rets = detector(gray, 1)
            if len(rets) > 0:
                shape = predictor(gray, rets[0])
                points = face_utils.shape_to_np(shape)
                mouse_points = points[MOUSE_START:MOUSE_END]

                # 使用cv2.convexHull获得位置的凸包位置
                mouseHull = cv2.convexHull(mouse_points)
                (x, y, w, h) = cv2.boundingRect(mouseHull)

                points_recorder_now = feature_standardization(mouse_points)

                sim = euclidean_distance(points_recorder_last, points_recorder_now)
                print(sim)
                total_count += 1

                if sim > 0.15:
                    moving_count += 1
                    print("lip moving...")
                else:
                    print("move too subtle..")

                points_recorder_last = points_recorder_now

                # 画出矩形 (0,255,9)是画线对应的rgb颜色、2是所画的线的宽度
                # border = 5
                # cv2.rectangle(frame, (x - border, y - border), (x + w + border, y + h + border), (0, 255, 9), 2)
                # 使用cv2.drawContours画出轮廓图
                # cv2.putText(frame, 'The mouth is detectable. ', (30, 30), font, 1, (0, 255, 255), 2)
                # print("detectable. ...")
                cv2.drawContours(frame, [mouseHull], -1, (0, 255, 0), 2)
            else:
                # cv2.putText(frame, 'Mouth is not detectable. ', (30, 30), font, 1, (0, 0, 255), 2)
                print("not detectable. ...")

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC退出
            break
        cv2.imshow("Frame", frame)

    # step 5: release
    cap.release()
    cv2.destroyAllWindows()

    # print("moving_count: ", moving_count)
    # print("total_count: ", total_count)

    if total_count != 0 and moving_count / total_count >= 0.3:
        return True
    else:
        return False


if __name__ == '__main__':
    if lip_tracking():
        print("okkk")
    else:
        print("not okkkk")
