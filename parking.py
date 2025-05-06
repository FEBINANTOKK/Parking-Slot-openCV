import cv2
import pickle
import numpy as np

cap = cv2.VideoCapture('./media/carPark.mp4')
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

width, height = 107, 48

def get_parking_status():
    cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) % cap.get(cv2.CAP_PROP_FRAME_COUNT))
    success, img = cap.read()
    freeSpaces, occupiedSpaces, suggested_slot = 0, 0, None
    imgProcessed = process_frame(img, cap)
    for idx, pos in enumerate(posList):
        x, y = pos
        imgCrop = imgProcessed[y:y+height, x:x+width]
        count = cv2.countNonZero(imgCrop)
        if count < 900:
            freeSpaces +=1
            if suggested_slot is None:
                suggested_slot = idx +1
        else:
            occupiedSpaces +=1
    return freeSpaces, occupiedSpaces, suggested_slot

def process_frame(img, cap):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold,5)
    kernel = np.ones((3,3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
    return imgDilate

def generate_video():
    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) % cap.get(cv2.CAP_PROP_FRAME_COUNT))
        success, img = cap.read()
        imgProcessed = process_frame(img, cap)
        for pos in posList:
            x, y = pos
            imgCrop = imgProcessed[y:y+height, x:x+width]
            count = cv2.countNonZero(imgCrop)
            if count < 900:
                color = (0,255,0)
                thickness = 5
            else:
                color = (0,0,255)
                thickness = 2
            cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, thickness)
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
