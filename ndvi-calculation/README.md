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
```

## Usage
 - Place your raster file (GeoTIFF format) in the data/ directory.
 - Run the script to calculate and plot NDVI:
```bash
 python src/calculate_ndvi.py
```

- The NDVI plot will be saved in the outputs/ directory.

```bash
ndvi-calculation/
├── src/                   # Source code
├── data/                  # Input data
├── outputs/               # Generated outputs
├── tests/                 # Test scripts
├── .gitignore             # Ignored files
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── LICENSE                # License file
```

## Sample NDVI Formula
NDVI is calculated as:

$$NDVI = \frac{(NIR - Red)}{(NIR + Red)}$$

Where:

 - NIR: Near-infrared band.
 - Red: Red band.
Example Output
![NDVI Plot](outputs/ndvi_plot.png "NDVI Plot")

Example dataset
- [eurosat](https://zenodo.org/records/7711810#.ZAm3k-zMKEA) 

References
 - [Sentinel-2 Data Overview](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-2) 
 - [eurosat](https://zenodo.org/records/7711810#.ZAm3k-zMKEA)

License

This project is licensed under the MIT Licens