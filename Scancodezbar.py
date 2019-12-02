""" scan_QR_code.py

Recognize QR code using camera.
Press Q to exit the program. 

Prerequisites:
    pip3 install pyzbar numpy opencv-python

"""

__DATE__ = "2019/10/22"

import pyzbar
import numpy as np
import cv2

CAMERA_INDEX = 1        # which camera to use

def process(img):
    """ Detect QR code and barcode in the image.

    @param img (numpy.ndarray): the image to be processed.
    @return (list): a list containing all the features detected.
    """
    # Find barcodes and QR codes
    objects = pyzbar.decode(img)

    for obj in objects:
        print("="*24)
        print(obj.rect)
        print("Type:", obj.type)
        print("Data:", obj.data, "\n")
     
    return objects


# Display barcode and QR code location  
def display(img, objects):
    """ Display barcode and QR code location.

    @param img (numpy.ndarray): the original image
    @param objects (list): detected features
    """
    for code in objects:
        points = code.polygon

        # If the points do not form a quad, find convex hull
        if len(points) > 4: 
            hull = cv2.convexHull(np.array(points, dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        
        # Number of points in the convex hull
        n = len(hull)

        # Draw the convext hull
        for j in range(0, n):
            cv2.line(img, hull[j], hull[(j+1) % n], (255, 0, 0), 3)
    
    # Display results 
    cv2.imshow("Result", img)

if __name__ == "__main__":
    cap = cv2.VideoCapture(CAMERA_INDEX)   # Start camera
    while True:
        img = cap.read()[1]
        objects = process(img)
        display(img, objects)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()