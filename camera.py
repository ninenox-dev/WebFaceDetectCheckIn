#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import cv2
from joblib import load
import numpy as np
import datetime


class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()

    def get_legacy_var(self):
        return "test"
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        clf = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
        demo_clf = load('ann-age-gender-v1.ml')  # โหลดไฟล์โมเดล

        #capture = cv2.VideoCapture(0)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            testlist = []
            face = gray[y:y + h, x:x + w]
            resized = cv2.resize(face, (200, 200), interpolation=cv2.INTER_LINEAR)
            testlist.append(np.ravel(resized))
            prediction = str(demo_clf.predict(testlist))

            probability = demo_clf.predict_proba(testlist)  # แสดงค่า probability
            print(probability)
            max_prob = max(probability[0])

            text = ''.join(prediction + ', conf: ' + '{0:.4g}'.format(max_prob * 100) + '%)')

            color = (255, 0, 0)
            if prediction.find('nisit') != -1:
                color = (255, 0, 255)

            # get the data
            now = datetime.datetime.now()
            # f = open("mod.txt","w+")
            # f.write(prediction+" : "+str(now)+"\n")
            # f.close

            with open('mod.txt', 'a') as the_file:
                the_file.write(prediction+" : "+str(now)+"\n")

            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, color)
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

        #cv2.imshow('my video', image)

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()