# import image of parking space
# mark every parking space as Region Of Interest
# works with fixed camera
import cv2
import pickle

# store clicked rectangles
width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)


while True:
    img = cv2.imread("./media/carParkImg.png")
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("image", img)
    cv2.setMouseCallback("image", mouseClick)

    # Wait for the user to press the "Esc" key to exit
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # 27 is the ASCII code for the Esc key
        break

# Close all OpenCV windows
cv2.destroyAllWindows()

print("code executed")
