import geopandas as gpd
from topojson import Topology
import json
import os

def convert_to_topojson(input_file, output_file):
    print(f"Reading {input_file}...")
    # Read the GeoJSON file
    gdf = gpd.read_file(input_file)
    
    print("Converting to TopoJSON...")
    # Convert to TopoJSON
    # We want to preserve the shapeName as a property
    topo = Topology(gdf, object_name='municipios', prequantize=False)
    
    # Convert to JSON
    topo_json = topo.to_json()
    
    # Parse the JSON string to a dict to modify it if necessary, or just write it
    topo_data = json.loads(topo_json)
    
    print(f"Writing to {output_file}...")
    with open(output_file, 'w') as f:
        json.dump(topo_data, f)
    
    print("Done!")

if __name__ == "__main__":
    input_geojson = 'angola_adm2.geojson'
    output_topojson = 'angola_municipios.topojson'
    
    if os.path.exists(input_geojson):
        convert_to_topojson(input_geojson, output_topojson)
    else:
        print(f"Error: {input_geojson} not found.")
