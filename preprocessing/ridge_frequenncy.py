import cv2
import numpy as np
import matplotlib.pyplot as plt



def load_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Image not found!")
    return img



def divide_into_blocks(img, block_size=32):
    h, w = img.shape
    blocks = []

    for i in range(0, h - block_size, block_size):
        for j in range(0, w - block_size, block_size):
            block = img[i:i+block_size, j:j+block_size]
            blocks.append(block)

    return blocks


def compute_fft(block):
    f = np.fft.fft2(block)
    fshift = np.fft.fftshift(f)
    magnitude = np.abs(fshift)
    return magnitude


def estimate_ridge_frequency(magnitude):
    center = magnitude.shape[0] // 2

    # Remove DC component
    magnitude[center-2:center+2, center-2:center+2] = 0

    # Find peak frequency
    peak = np.unravel_index(np.argmax(magnitude), magnitude.shape)

    distance = np.sqrt((peak[0] - center)**2 + (peak[1] - center)**2)

    if distance == 0:
        return 0

    ridge_frequency = distance / magnitude.shape[0]
    return ridge_frequency


def process_image(path):
    img = load_image(path)
    blocks = divide_into_blocks(img)

    frequencies = []

    for block in blocks:
        mag = compute_fft(block)
        freq = estimate_ridge_frequency(mag)
        frequencies.append(freq)

    return img, blocks, frequencies


def visualize_fft(block):
    magnitude = compute_fft(block)

    plt.figure(figsize=(6, 6))
    plt.imshow(np.log(magnitude + 1), cmap='gray')
    plt.title("FFT Magnitude Spectrum")
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    image_path = "fingerprint_sample.jpg"   # replace with your image

    img, blocks, freqs = process_image(image_path)

    print("Average Ridge Frequency:", np.mean(freqs))

    # Visualize first block spectrum
    visualize_fft(blocks[0])
