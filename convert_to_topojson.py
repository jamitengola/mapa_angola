import json
import geopandas as gpd
from topojson import Topology

# Load the GeoJSON file
geojson_path = 'angola_21_provincias.geojson'
gdf = gpd.read_file(geojson_path)

# Convert to TopoJSON
# We want to preserve the topology
topo = Topology(gdf, object_name='provincias', prequantize=False)

# Save to file
topojson_path = 'angola_21_provincias.topojson'
topo.to_json(topojson_path)

print(f"Converted {geojson_path} to {topojson_path}")
