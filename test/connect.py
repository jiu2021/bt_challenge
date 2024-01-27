import cv2
import numpy as np

# 加载要拼接的5个视频
video1 = cv2.VideoCapture('group1_erp.mp4')
video2 = cv2.VideoCapture('group1_cmp.mp4')
video3 = cv2.VideoCapture('benchmark.mp4')
video4 = cv2.VideoCapture('group1_eac.mp4')
video5 = cv2.VideoCapture('group1_free.mp4')

# 获取每个视频的帧尺寸
frame_width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建输出视频的写入器
output_video = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width * 5, frame_height))

while True:
    # 读取每个视频的帧
    ret1, frame1 = video1.read()
    ret2, frame2 = video2.read()
    ret3, frame3 = video3.read()
    ret4, frame4 = video4.read()
    ret5, frame5 = video5.read()

    # 如果所有视频的帧都读取完毕，则退出循环
    if not (ret1 and ret2 and ret3 and ret4 and ret5):
        break

    # 在空间上拼接每个视频的帧
    output_frame = np.concatenate((frame1, frame2, frame3, frame4, frame5), axis=1)

    # 写入输出视频
    output_video.write(output_frame)

# 释放视频对象和关闭输出视频写入器
video1.release()
video2.release()
video3.release()
video4.release()
video5.release()
output_video.release()