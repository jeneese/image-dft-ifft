# Discrete Fourier Transform and Inverse Discrete Fourier Transform of an Image

This Python script performs the [Discrete Fourier Transform](https://en.wikipedia.org/wiki/Discrete_Fourier_transform) on an image by applying a Fast Fourier Transform on each row of an image followed by each column to generate plots of the Magnitude and Phase spectrum of the original image. Then, the script performs the [Inverse Fast Fourier Transform](https://en.wikipedia.org/wiki/Discrete-time_Fourier_transform#Inverse_transform) by taking the complex conjugate of the image, performing the DFT, and taking the real component of the complex conjugate to generate plots of the original image and the image restored by IFFT.

## Installation

Use the package manager pip to install Opencv, Numpy and Matplotlib

```bash
pip install opencv-python
pip install numpy
pip install matplotlib
```

## Usage

After running the program in Python, one prompt will appear.

```
Type the path with file extension of the image file you'd like to test:
```

Enter an absolute or relative path for your image.

The program will then begin to evaluate the image and generate a magnitude and phase spectrum plot. After the first plot is closed, a second plot will be displayed of the original image and the image generated using IFFT.
