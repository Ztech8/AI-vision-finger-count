import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize HandDetector with a detection confidence of 0.8 and allow tracking of only one hand
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Open the default camera (camera index 0)
camera = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, video = camera.read()

    # Use the HandDetector to find hands in the frame
    hands, img = detector.findHands(video)

    # Check if hands are detected
    if hands:
        # Get information about the first detected hand
        List = hands[0]

        # Get the status of fingers (0 for closed, 1 for open) from HandDetector
        fingerUp = detector.fingersUp(List)

        # Print the status of fingers
        print(fingerUp)

        # Check if all fingers are closed (0)
        if fingerUp == [0, 0, 0, 0, 0]:
            # Display a message if all fingers are closed
            cv2.putText(video, "finger Count: 0", (20, 460), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1, cv2.LINE_AA)

    # Display the processed frame
    cv2.imshow('Frame', video)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
