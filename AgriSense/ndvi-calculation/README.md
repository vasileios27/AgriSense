# NDVI Calculation and Visualization

This project calculates and visualizes the Normalized Difference Vegetation Index (NDVI) from Sentinel-2 imagery. NDVI is widely used to measure vegetation health and is derived using the red and near-infrared (NIR) bands of satellite data.

## Features
- Calculates NDVI from a raster file (GeoTIFF format).
- Generates and saves an NDVI plot.
- Supports Sentinel-2 data with the ability to customize band selection.

## Requirements
- **Python 3.8+**
- **Dependencies**:
  - rasterio
  - numpy
  - matplotlib

Install the dependencies using:
```bash
pip install -r requirements.txt
