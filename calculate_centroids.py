import geopandas as gpd
import pandas as pd

def calculate_centroids(input_file, output_file):
    print(f"Reading {input_file}...")
    gdf = gpd.read_file(input_file)
    
    # Reproject to a projected CRS to calculate centroids accurately, then project back
    # EPSG:3857 is a common choice for web maps (Pseudo-Mercator), or we can use a local one.
    # For simplicity and since we just want a label point, using the geographic centroid is usually fine for visualization.
    # However, warning: Geometry is in a geographic CRS. Results from 'centroid' are likely incorrect.
    # So we should project first. Angola is roughly UTM zone 33S (EPSG:32733).
    
    gdf_projected = gdf.to_crs(epsg=32733)
    centroids = gdf_projected.centroid
    centroids_geo = centroids.to_crs(gdf.crs)
    
    # Create a DataFrame with names and coordinates
    # Assuming 'shapeName' is the column with province names
    df = pd.DataFrame({
        'Province': gdf['shapeName'],
        'Latitude': centroids_geo.y,
        'Longitude': centroids_geo.x
    })
    
    print(f"Writing centroids to {output_file}...")
    df.to_csv(output_file, index=False)
    print("Done!")

if __name__ == "__main__":
    calculate_centroids('angola_21_provincias.geojson', 'angola_21_provincias_centroids.csv')
