#!/usr/bin/env Python
# coding=utf-8

import cv2
import numpy as np
 
img = cv2.imread('QR2.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
 
result_detection = None
count_experiments = 10
transform = None
qrcode = cv2.QRCodeDetector()
 
for i in range(count_experiments):
    # 检测与识别
    result_detection,transform,straight_qrcode = qrcode.detectAndDecode(img_gray)
    
    if result_detection:
        print('result',result_detection)
        break
