import cv2
import numpy as np
from matplotlib import pyplot as plt

def DFT2(f):
    """ Function performs FFT on each row of an image followed by each column to perform DFT2
        params:
            f: scaled version of greyscale image
        """
    image = f

    imageWidth = image.shape[1]  #Saves the number of horizontal pixels to imageWidth
    imageHeight = image.shape[0]  #Saves the number of vertical pixels to imageHeight

    transform = np.zeros(shape = (imageHeight,imageWidth),dtype='complex') #Creates a complex array filled with zeros

    xPosition = 0
    yPosition = 0

    #FFT is taken of each row of pixels in the image first, followed by each column of pixels in the image
    while (yPosition < imageHeight):  # Loops through each column
        while (xPosition < imageWidth):  # Loops through each row
            transform[:,xPosition] = np.fft.fft(image[:,xPosition])
            xPosition = xPosition + 1
        transform[yPosition,:] = np.fft.fft(transform[yPosition,:])
        yPosition = yPosition + 1

    return transform

def IFFT(F):
    """ Function performs IFFT by taking complex conjugate, performing DFT2, taking the real component of the complex conjugate, and dividing by MN
        params:
            F: image returned after DFT2
        """

    transform = F

    imageWidth = transform.shape[1] #Saves the number of horizontal pixels to imageWidth (M)
    imageHeight = transform.shape[0] #Saves the number of vertical pixels to imageHeight (N)

    #The complex conjugate is taken of transformed image, followed by the dft2, and then the real component of the complex conjugate
    conj_transform = np.conjugate(transform)
    conj_g = DFT2(conj_transform)
    g = np.real(np.conjugate(conj_g))

    #The result is divided by M*N and multiplied by 255 to account for scaling
    g = 255*(g/(imageWidth*imageHeight))

    return g

def main(): #Main begins
    file = input("Type the path with file extension of the image file you'd like to test:")  # User enter .png file for testing
    image = cv2.imread(file,0)  # Saves the image input typed in by the user to image

    image_scaled = image / 255
    f = image_scaled

    F = DFT2(f)

    #FFT shift is used to rearrange zero frequency components to the center
    F_shifted = np.fft.fftshift(F)
    magnitude_F = np.log(1 + np.abs(F_shifted))
    phase_F = np.angle(F_shifted)

    #Generates the plot of the magnitude spectrum and the phase spectrum
    plt.subplot(121), plt.imshow(magnitude_F, cmap='gray')
    plt.title("Magnitude Spectrum")
    plt.subplot(122), plt.imshow(phase_F, cmap='gray')
    plt.title("Phase Spectrum")
    plt.show()

    g = IFFT(F)

    #Generates the plot of the original image and the restored image using IFFT
    plt.subplot(121), plt.imshow(f, cmap='gray')
    plt.title("f:Original selected image")
    plt.subplot(122), plt.imshow(g, cmap='gray')
    plt.title("g:Image generated by IFFT")
    plt.show()

if __name__ == "__main__":
    main()