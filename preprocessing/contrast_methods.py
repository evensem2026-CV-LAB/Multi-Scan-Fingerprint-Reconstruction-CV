import cv2
import numpy as np
import os


def histogram_equalization(img):
    return cv2.equalizeHist(img)


def clahe_enhancement(img, clip=2.0, grid=(8,8)):
    clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=grid)
    return clahe.apply(img)


def adaptive_contrast_stretch(img):
    min_val = np.min(img)
    max_val = np.max(img)
    stretched = (img - min_val) * (255 / (max_val - min_val + 1e-8))
    return stretched.astype(np.uint8)


def compare_methods(img_path, output_folder="outputs"):
    os.makedirs(output_folder, exist_ok=True)

    img = cv2.imread(img_path, 0)

    he = histogram_equalization(img)
    clahe = clahe_enhancement(img)
    stretch = adaptive_contrast_stretch(img)

    cv2.imwrite(f"{output_folder}/hist_eq.png", he)
    cv2.imwrite(f"{output_folder}/clahe.png", clahe)
    cv2.imwrite(f"{output_folder}/contrast_stretch.png", stretch)

    print("Contrast enhancement outputs saved.")


if __name__ == "__main__":
    compare_methods("../data/sample1.png")
