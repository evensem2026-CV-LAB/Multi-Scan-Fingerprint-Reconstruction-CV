# Methodology

This section details the classical computer vision pipeline used to reconstruct high-quality fingerprints from multiple low-quality scans.

## 1. Multi-Capture Acquisition
The process begins by capturing **3 to 5 images** of the same finger. This redundancy is crucial for overcoming localized noise and artifacts present in individual scans.

## 2. Preprocessing
To prepare the raw images for alignment and fusion, each scan undergoes preprocessing:
- **Histogram Equalization**: Improves the global contrast of the fingerprint image.
- **Noise Filtering**: Uses Gaussian or Median filtering to reduce high-frequency noise while preserving ridge structures.

## 3. Registration (Alignment)
Since the user may place their finger slightly differently for each scan, the images must be perfectly aligned. We use a **ridge orientation-based registration** method:
- **Feature Extraction**: Detect minutiae points and ridge orientation fields.
- **Transformation**: Calculate the optimal rotation and translation parameters to align all secondary images to the primary (reference) image.

## 4. Confidence-Weighted Fusion
Once aligned, the images are fused. Instead of simple averaging, we use a **confidence-weighted approach**:
- Areas with higher clarity and distinct ridge patterns are given higher weights.
- Noisy or blurred regions contribute less to the final image.
This ensures that the best parts of each scan are preserved.

## 5. DWT-Based Enhancement
The fused image is further enhanced using **Discrete Wavelet Transform (DWT)**:
- Decomposes the image into frequency sub-bands.
- Enhances ridge details in high-frequency bands.
- Reconstructs the image to sharpen ridges and suppress background noise.

## 6. Output and Visualization
The final output is a high-resolution, reconstructed fingerprint. The system provides visualizations of:
- Original low-quality scans
- Preprocessed images
- Registration overlay (showing alignment accuracy)
- Final fused and enhanced result
