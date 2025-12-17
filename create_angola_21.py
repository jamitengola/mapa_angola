import geopandas as gpd
import json

# Load ADM2
gdf = gpd.read_file('angola_adm2.geojson')

# Define mapping
mapping = {
    "Bengo": ["Ambriz", "Bula-Atumba", "Dande", "Dembos-Quibaxe", "Nambuangongo", "Pango-Aluquem"],
    "Benguela": ["Baia Farta", "Balombo", "Benguela", "Bocoio", "Caimbambo", "Chongoroi", "Cubal", "Ganda", "Lobito"],
    "Bié": ["Andulo", "Camacupa", "Catabola", "Chinguar", "Chitembo", "Cuemba", "Cunhinga", "Cuito", "N'harea"],
    "Cabinda": ["Belize", "Buco Zau", "Cabinda", "Cacongo (Landana)"],
    "Cuando": ["Dirico", "Mavinga", "Rivungo"],
    "Cuanza Norte": ["Ambaca", "Banga", "Bolongongo", "Cambambe", "Cazengo", "Golungo Alto", "Lucala", "Ngonguembo", "Quiculongo", "Samba Caju"],
    "Cuanza Sul": ["Amboim (Gabela)", "Cassongue", "Cela (Waku Kungo)", "Conda", "Ebo", "Libolo (Calulo)", "Mussende", "Porto Amboim", "Quibala", "Quilenda", "Seles (Uku Seles)", "Sumbe (Ngangula)"],
    "Cubango": ["Calai", "Cuangar", "Cuchi", "Menongue", "Nancova", "Cuito Cuanavale"],
    "Cunene": ["Cahama", "Cuanhama", "Curoca", "Cuvelai", "Namacunde", "Ombadja"],
    "Huambo": ["Bailundo", "Caala", "Catchiungo", "Ecunha (Ekunha)", "Huambo", "Londuimbale", "Longonjo", "Mungo", "Tchikala-Tcholohanga", "Tchinjenje", "Ukuma"],
    "Huíla": ["Caconda", "Caluquembe", "Chibia", "Chicomba", "Chipindo", "Cuvango", "Gambos(Chiange)", "Humpata", "Jamba", "Lubango", "Matala", "Quilengues", "Quipungo"],
    "Ícolo e Bengo": ["Icolo e Bengo", "Quissama"],
    "Luanda": ["Belas", "Cacuaco", "Luanda"],
    "Lunda Norte": ["Cambulo", "Capenda-Camulemba", "Caungula", "Chitato", "Cuango", "Cuilo", "Lubalo", "Lucapa", "Xa-Muteba"],
    "Lunda Sul": ["Cacolo", "Dala", "Muconda", "Saurimo"],
    "Malanje": ["Cacuso", "Cahombo", "Calandula", "Cambundi-Catembo", "Cangandala", "Cunda-dia-Baze", "Kiuaba-N'Zoji", "Luquembo", "Malanje", "Marimba", "Massango", "Mucari", "Quela", "Quirima"],
    "Moxico": ["Camanongue", "Leua", "Luchazes", "Luena", "Bundas"],
    "Moxico Leste": ["Alto Zambeze", "Cameia (Lumeje)", "Luacano", "Luau"],
    "Namibe": ["Bibala", "Camucuio", "Namibe", "Tombwa", "Virei"],
    "Uíge": ["Ambuila", "Bembe", "Buengas", "Bungo", "Cangola", "Damba", "Maquela do Zombo", "Milunga", "Mucaba", "Negage", "Puri", "Quimbele", "Quitexe", "Sanza Pombo", "Songo", "Uige"],
    "Zaire": ["Cuimba", "Mbanza Congo", "N'Zeto", "Noqui", "Soyo", "Tomboco"]
}

# Invert mapping to Municipality -> Province
mun_to_prov = {}
for prov, muns in mapping.items():
    for mun in muns:
        mun_to_prov[mun] = prov

# Assign new province
def get_province(row):
    name = row['shapeName']
    return mun_to_prov.get(name, "Unknown")

gdf['NewProvince'] = gdf.apply(get_province, axis=1)

# Check for unknowns
unknowns = gdf[gdf['NewProvince'] == "Unknown"]
if not unknowns.empty:
    print("Warning: The following municipalities were not mapped:")
    print(unknowns['shapeName'].tolist())

# Dissolve
gdf_prov = gdf.dissolve(by='NewProvince')

# Reset index to make NewProvince a column
gdf_prov = gdf_prov.reset_index()

# Keep only relevant columns
gdf_prov = gdf_prov[['NewProvince', 'geometry']]
gdf_prov = gdf_prov.rename(columns={'NewProvince': 'shapeName'})

# Save
gdf_prov.to_file('angola_21_provincias.geojson', driver='GeoJSON')
print("Successfully created angola_21_provincias.geojson")
