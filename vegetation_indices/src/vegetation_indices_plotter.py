import rasterio
import numpy as np
import matplotlib.pyplot as plt

# File path to the raster file
file_path = "../data/sample_data.tif"

# Vegetation index functions
def ndvi(nir, red):
    return (nir - red) / (nir + red)

def evi(nir, red, blue):
    return 2.5 * (nir - red) / (nir + 6 * red - 7.5 * blue + 1)

def savi(nir, red, L=0.5):
    return (nir - red) / (nir + red + L) * (1 + L)

def gndvi(nir, green):
    return (nir - green) / (nir + green)

def msavi(nir, red):
    return 0.5 * (2 * nir + 1 - np.sqrt((2 * nir + 1)**2 - 8 * (nir - red)))

# Load the raster file
with rasterio.open(file_path) as src:
    red = src.read(4)     # Band 4 - Red
    nir = src.read(8)     # Band 8 - Near Infrared
    green = src.read(3)   # Band 3 - Green
    blue = src.read(2)    # Band 2 - Blue

# Calculate vegetation indices
indices = {
    "NDVI": ndvi(nir, red),
    "EVI": evi(nir, red, blue),
    "SAVI": savi(nir, red),
    "GNDVI": gndvi(nir, green),
    "MSAVI": msavi(nir, red)
}

# Plot and save each vegetation index
for name, index in indices.items():
    plt.figure(figsize=(8, 8))
    plt.imshow(index, cmap="RdYlGn")
    plt.colorbar(label=name)
    plt.title(f"{name} - Vegetation Index")
    plt.axis("off")
    output_file = f"../outputs/{name}_plot.png"
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"{name} plot saved at {output_file}")
    plt.show()
