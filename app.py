import requests
import os
import numpy as np
import rasterio
import geopandas as gpd
from shapely.geometry import Polygon
from dino import GroundingDino
from segment_anything import SegmentAnything


##################################################
# Download latest sea ice GeoTIFF image ##########

url = "https://umbra.nascom.nasa.gov/cgi-bin/mosaic?product=sea_ice_tpn&date=latest&resolution=250m"
filename = "latest_sea_ice_tpn.tif"

response = requests.get(url)
if response.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(response.content)

##################################################
# Load GeoTIFF image into numpy array ############

with rasterio.open(filename) as src:
    data = src.read()
    profile = src.profile
    bounds = src.bounds
    transform = src.transform

##################################################
# Segment the image using SAM model ##############

model = SegmentAnything()
segmentation = model.predict(data)

##################################################
# Convert results to GeoDataFrame and save file ##

polygons = []
for i, seg in enumerate(segmentation):
    polygon = Polygon(rasterio.features.shapes(seg, transform=transform)[0][1])
    polygons.append(polygon)
gdf = gpd.GeoDataFrame({'geometry': polygons})
gdf.to_file('segmentation_results.gpkg', driver='GPKG')

##################################################
# Use GroundingDino to label the result polygons #

dino = GroundingDino()
labels = dino.label('segmentation_results.gpkg')

