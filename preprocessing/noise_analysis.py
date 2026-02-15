import cv2
import numpy as np
import os

def add_gaussian_noise(image, mean=0, var=10):
    sigma = var ** 0.5
    gaussian = np.random.normal(mean, sigma, image.shape)
    noisy = image + gaussian
    noisy = np.clip(noisy, 0, 255)
    return noisy.astype(np.uint8)

def apply_gaussian_filter(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def apply_median_filter(image):
    return cv2.medianBlur(image, 5)

def main():
    # Create output folder
    os.makedirs("outputs", exist_ok=True)

    # Load fingerprint image
    image = cv2.imread("data/sample1.png", 0)

    if image is None:
        print("Image not found. Put sample1.png inside data folder.")
        return

    # Add synthetic noise (for demonstration)
    noisy_image = add_gaussian_noise(image)

    # Apply filters
    gaussian_result = apply_gaussian_filter(noisy_image)
    median_result = apply_median_filter(noisy_image)

    # Save results
    cv2.imwrite("outputs/original.png", image)
    cv2.imwrite("outputs/noisy.png", noisy_image)
    cv2.imwrite("outputs/gaussian_filtered.png", gaussian_result)
    cv2.imwrite("outputs/median_filtered.png", median_result)

    print("Noise analysis completed. Check outputs folder.")

if __name__ == "__main__":
    main()
