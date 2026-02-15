# Multi-Scan Fingerprint Reconstruction

## Problem Statement
Biometric systems often struggle with enhancing weak and low-quality fingerprints, particularly those from elderly users. Traditional single-image enhancement techniques may fail to recover sufficient ridge detail for reliable matching.

## Key Idea
This project implements a classical computer-vision pipeline that utilizes **multi-capture fusion**. Instead of relying on a single scan, we acquire 3–5 scans of the same finger, align them, and fuse them to reconstruct a high-quality fingerprint. This approach is:
- **Lightweight**: Optimized for low-power devices.
- **Non-Deep Learning**: Uses classical image processing techniques for explainability and speed.
- **Cost-Effective**: Designed for deployment in low-cost biometric centers like e-Mitra.

## Pipeline Overview
The reconstruction process follows these steps:
1.  **Multi-Capture Acquisition**: Capture 3-5 images of the same finger.
2.  **Preprocessing**: Apply histogram equalization and noise filtering.
3.  **Registration**: Align images using ridge orientation-based registration.
4.  **Fusion**: Combine aligned images using confidence-weighted fusion.
5.  **Enhancement**: Apply DWT-based enhancement and restoration.
6.  **Output**: Generate a final reconstructed fingerprint with improved ridge clarity.

## Team
We are a team of students working on this computer vision project.

- [Chirag Taneja](chirag_102323072/index.md)
- [Ansh](ansh_102323077/index.md)
- [Lakshit](lakshit_102323059/index.md)
- [Siddhi](siddhi_102323065/index.md)
