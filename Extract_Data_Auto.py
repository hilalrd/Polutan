
import os
import glob
import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd
from shapely.geometry import mapping

def find_file(extension):
    """Find the first file in the current directory with the specified extension."""
    files = glob.glob(f"./*.{extension}")
    if not files:
        raise FileNotFoundError(f"No .{extension} file found in the current directory.")
    return files[0]

def plot_co_dki_jakarta(co_file_path, shapefile_path):
    # Load shapefile for DKI Jakarta
    dki_jakarta = gpd.read_file(shapefile_path)

    # Determine boundaries
    min_lat = dki_jakarta.bounds.miny.min()
    max_lat = dki_jakarta.bounds.maxy.max()
    min_lon = dki_jakarta.bounds.minx.min()
    max_lon = dki_jakarta.bounds.maxx.max()

    # Load CO data from NetCDF file
    data = xr.open_dataset(co_file_path, group='PRODUCT')
    co_data = data['carbonmonoxide_total_column_corrected']

    # Handle 3D or 2D data dimensions
    if co_data.ndim == 3:
        co_values_dki = co_data.isel(time=0)
    elif co_data.ndim == 2:
        co_values_dki = co_data
    else:
        raise ValueError(f"Unsupported CO data dimensions: {co_data.ndim}")

    # Extract latitude and longitude
    longitude = co_values_dki['longitude'].values
    latitude = co_values_dki['latitude'].values

    # Create meshgrid for coordinates
    if longitude.ndim == 1 and latitude.ndim == 1:
        lon2d, lat2d = np.meshgrid(longitude, latitude)
    elif longitude.ndim == 2 and latitude.ndim == 2:
        lon2d, lat2d = longitude, latitude
    else:
        raise ValueError("Longitude and latitude dimensions are inconsistent.")

    # Create mask for DKI Jakarta boundaries
    mask = (lat2d >= min_lat) & (lat2d <= max_lat) & (lon2d >= min_lon) & (lon2d <= max_lon)
    co_filtered = np.where(mask, co_values_dki.values, np.nan)

    # Plot data
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.set_extent([min_lon, max_lon, min_lat, max_lat], crs=ccrs.PlateCarree())
    contour = ax.contourf(lon2d, lat2d, co_filtered, 60, cmap='viridis', transform=ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE, linewidth=0.5)
    ax.add_feature(cfeature.BORDERS, linewidth=0.5)
    ax.add_feature(cfeature.LAND, facecolor="lightgray")
    ax.add_feature(cfeature.LAKES, facecolor="lightblue")
    ax.add_feature(cfeature.RIVERS, linewidth=0.5)
    cbar = fig.colorbar(contour, ax=ax, orientation='vertical', label='CO Concentration (mol/m²)')
    ax.set_title('CO Concentration Distribution in DKI Jakarta')

    # Save the plot
    output_path = "CO_Distribution_DKI_Jakarta.png"
    plt.savefig(output_path, dpi=300)
    print(f"Plot saved to {output_path}")
    plt.show()

if __name__ == "__main__":
    # Automatically locate files
    nc_file = find_file("nc")
    shp_file = find_file("shp")

    # Generate plot for CO data in DKI Jakarta
    plot_co_dki_jakarta(nc_file, shp_file)
