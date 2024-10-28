import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector

#from cvzone.HandTrackingModule import HandDetector
#import cv2

# Initialize the webcam to capture video
# The '2' indicates the third camera connected to your computer; '0' would usually refer to the built-in camera
cap = cv2.VideoCapture(0)
cap.set(propId=3, value=1280)
cap.set(propId=4, value=720)


# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1 , modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)


def getHandInfo(img):
    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand = hands[0]  # Get the first hand detected
        lmList = hand["lmList"]  # List of 21 landmarks for the first hand
     
        # Count the number of fingers up for the first hand
        fingers = detector.fingersUp(hand)
        print(fingers)  # Print the count of fingers that are up
        return fingers, lmList
    else:
        return None
def draw(info, prev_pos, canvas):
    fingers, lm
        # Calculate distance between specific landmarks on the first hand and draw it on the image
        length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[12][0:2], img, color=(255, 0, 255),
                                                  scale=10)


    # Display the image in a window
    cv2.imshow("Image", img)

    # Keep the window open and update it for each frame; wait for 1 millisecond between frames
    cv2.waitKey(1)