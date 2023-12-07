import cv2
import numpy as np
import tensorflow as tf
import os



def main():
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Cannot open camera")
        return
    

    while True:
        # capture frame-by-frame
        ret, frame = cam.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (616, 616), interpolation=cv2.INTER_CUBIC)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) == ord('q'):
            cv2.imwrite('img1.jpg', gray)
            break

    # When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()

    #Read the temporarily stored image into memory for preprocessing 
    img = cv2.imread('img1.jpg', cv2.IMREAD_GRAYSCALE)

    #Prompt the user to confirm whether to procedd with the image
    cv2.imshow("Captured image. To proceed press y else to discard press n", img)

    #If user does not like the image, they can discard it and the program terminates
    if cv2.waitKey(0) == ord('n'):
        cv2.destroyAllWindows()
        print("Program terminated. Captured image discarded")
        os.remove('img1.jpg')
        return
    
    #Otherwise we proceed
    elif cv2.waitKey(1) == ord('y'):
        cv2.destroyAllWindows() 

    #Changes the image to completely black and white
    img = cv2.threshold(img, 65, 255, cv2.THRESH_BINARY)[1]

    #This is optional code to view the image after being pre processed
    """cv2.imshow('frame', img)
    cv2.waitKey()
    cv2.destroyAllWindows()"""

    #Since the training data contained white digits against dark background, we also do that to the input image
    img = cv2.bitwise_not(img)

    #Resize and reshape the image so that it properly matches the dimensions of the input layer of the neural network 
    img = cv2.resize(img, (28, 28))
    #optional code to view thw image which is being fed to the network. It will be a small 28*28 black and white image
    """cv2.imshow('frame', img)
    cv2.waitKey()
    cv2.destroyAllWindows()"""
    img = img.reshape(1, 28, 28, 1)

    #Load the model
    model = tf.keras.models.load_model('digpred.h5')

    #Make prediction and change the encoded output back to human digits
    print(f"The digit was {np.argmax(model.predict(img))}")

    #Finally delete the temporarily stored image
    os.remove('img1.jpg')




if __name__ == "__main__":
    main()