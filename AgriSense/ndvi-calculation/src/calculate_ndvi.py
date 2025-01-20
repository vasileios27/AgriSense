import rasterio
import numpy as np
from rasterio.plot import show
import matplotlib.pyplot as plt

# File path to the raster file
file_path = "../data/sample_data.tif"

# Open the Sentinel-2 raster file
with rasterio.open(file_path) as src:
    # Read the red and near-infrared bands
    red = src.read(4)
    nir = src.read(8)

    # Calculate the NDVI
    ndvi = (nir - red) / (nir + red)

# Plot and save the NDVI
plt.figure(figsize=(10, 10))
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(label='NDVI')
plt.title('NDVI Plot')
plt.axis('off')

# Save the plot
output_file = "../outputs/ndvi_plot.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"Plot saved at {output_file}")

# Show the plot
plt.show()
