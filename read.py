import cv2 as cv

#reading images
# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)
# cv.waitKey(0)
def rescaleFrame(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('Videos/dog.mp4')

def changeRes(width, height): #For Live video only
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.5)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'): #If letter d is pressed then it will end
        break


capture.release()
cv.destroyAllWindows()
