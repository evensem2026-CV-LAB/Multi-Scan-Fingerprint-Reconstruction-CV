# Preprocessing

Preprocessing is a critical step in the fingerprint reconstruction pipeline, especially for elderly users whose fingerprints may have low contrast or worn-out ridges.

## Why Preprocessing?
Elderly fingerprints often suffer from:
- **Low Contrast**: Faint ridges that are hard to distinguish from valleys.
- **Dry/Wet Skin**: Causing broken or smudged ridges.
- **Noise**: Sensor noise or skin artifacts.

Preprocessing enhances these images to make subsequent alignment and fusion steps more robust.

## Contrast Enhancement
We utilize **Histogram Equalization** (HE) and **Adaptive Histogram Equalization** (CLAHE) to improve local contrast.
- **HE**: Spreads out the most frequent intensity values.
- **CLAHE**: Enhances contrast in small tile regions, preventing noise amplification in uniform areas.

## Noise Removal
To remove random noise while preserving ridge edges, we apply:
- **Gaussian Smoothing**: To smooth out graininess.
- **Median Filtering**: Effective at removing "salt and pepper" noise common in sensor captures.

## Ridge Clarity Improvement
After basic enhancement, the ridge structures become more distinct, allowing the registration algorithm to accurately detect orientation fields and minutiae points.
