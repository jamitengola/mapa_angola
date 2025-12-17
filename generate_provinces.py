import json

municipalities = [
    "Alto Zambeze", "Ambaca", "Amboim (Gabela)", "Ambriz", "Ambuila", "Andulo", "Baia Farta", "Bailundo", "Balombo", "Banga", 
    "Belas", "Belize", "Bembe", "Benguela", "Bibala", "Bocoio", "Bolongongo", "Buco Zau", "Buengas", "Bula-Atumba", 
    "Bundas", "Bungo", "Caala", "Cabinda", "Cacolo", "Caconda", "Cacongo (Landana)", "Cacuaco", "Cacuso", "Cahama", 
    "Cahombo", "Caimbambo", "Calai", "Calandula", "Caluquembe", "Camacupa", "Camanongue", "Cambambe", "Cambulo", "Cambundi-Catembo", 
    "Cameia (Lumeje)", "Camucuio", "Cangandala", "Cangola", "Capenda-Camulemba", "Cassongue", "Catabola", "Catchiungo", "Caungula", "Cazengo", 
    "Cela (Waku Kungo)", "Chibia", "Chicomba", "Chinguar", "Chipindo", "Chitato", "Chitembo", "Chongoroi", "Conda", "Cuangar", 
    "Cuango", "Cuanhama", "Cubal", "Cuchi", "Cuemba", "Cuilo", "Cuimba", "Cuito", "Cuito Cuanavale", "Cunda-dia-Baze", 
    "Cunhinga", "Curoca", "Cuvango", "Cuvelai", "Dala", "Damba", "Dande", "Dembos-Quibaxe", "Dirico", "Ebo", 
    "Ecunha (Ekunha)", "Gambos(Chiange)", "Ganda", "Golungo Alto", "Huambo", "Humpata", "Icolo e Bengo", "Jamba", "Kiuaba-N'Zoji", "Leua", 
    "Libolo (Calulo)", "Lobito", "Londuimbale", "Longonjo", "Luacano", "Luanda", "Luau", "Lubalo", "Lubango", "Lucala", 
    "Lucapa", "Luchazes", "Luena", "Luquembo", "Malanje", "Maquela do Zombo", "Marimba", "Massango", "Matala", "Mavinga", 
    "Mbanza Congo", "Menongue", "Milunga", "Mucaba", "Mucari", "Muconda", "Mungo", "Mussende", "N'Zeto", "N'harea", 
    "Namacunde", "Nambuangongo", "Namibe", "Nancova", "Negage", "Ngonguembo", "Noqui", "Ombadja", "Pango-Aluquem", "Porto Amboim", 
    "Puri", "Quela", "Quibala", "Quiculongo", "Quilenda", "Quilengues", "Quimbele", "Quipungo", "Quirima", "Quissama", 
    "Quitexe", "Rivungo", "Samba Caju", "Sanza Pombo", "Saurimo", "Seles (Uku Seles)", "Songo", "Soyo", "Sumbe (Ngangula)", "Tchikala-Tcholohanga", 
    "Tchinjenje", "Tomboco", "Tombwa", "Uige", "Ukuma", "Virei", "Xa-Muteba"
]

# Mapping based on the new 21 provinces
provinces = {
    "Bengo": ["Ambriz", "Bula-Atumba", "Dande", "Dembos-Quibaxe", "Nambuangongo", "Pango-Aluquem"],
    "Benguela": ["Baia Farta", "Balombo", "Benguela", "Bocoio", "Caimbambo", "Chongoroi", "Cubal", "Ganda", "Lobito"],
    "Bié": ["Andulo", "Camacupa", "Catabola", "Chinguar", "Chitembo", "Cuemba", "Cunhinga", "Cuito", "N'harea"],
    "Cabinda": ["Belize", "Buco Zau", "Cabinda", "Cacongo (Landana)"],
    "Cuando": ["Cuito Cuanavale", "Dirico", "Mavinga", "Rivungo"],
    "Cuanza Norte": ["Ambaca", "Banga", "Bolongongo", "Bungo", "Cambambe", "Cazengo", "Golungo Alto", "Lucala", "Ngonguembo", "Quiculongo", "Samba Caju"], # Bungo is Uige, wait.
    "Cuanza Sul": ["Amboim (Gabela)", "Cassongue", "Cela (Waku Kungo)", "Conda", "Ebo", "Libolo (Calulo)", "Mussende", "Porto Amboim", "Quibala", "Quilenda", "Seles (Uku Seles)", "Sumbe (Ngangula)"],
    "Cubango": ["Calai", "Cuangar", "Cuchi", "Menongue", "Nancova"],
    "Cunene": ["Cahama", "Cuanhama", "Curoca", "Cuvelai", "Namacunde", "Ombadja"],
    "Huambo": ["Bailundo", "Caala", "Catchiungo", "Ecunha (Ekunha)", "Huambo", "Londuimbale", "Longonjo", "Mungo", "Tchikala-Tcholohanga", "Tchinjenje", "Ukuma"],
    "Huíla": ["Caconda", "Caluquembe", "Chibia", "Chicomba", "Chipindo", "Cuvango", "Gambos(Chiange)", "Humpata", "Jamba", "Lubango", "Matala", "Quilengues", "Quipungo"],
    "Ícolo e Bengo": ["Icolo e Bengo", "Quissama"],
    "Luanda": ["Belas", "Cacuaco", "Luanda"],
    "Lunda Norte": ["Cambulo", "Capenda-Camulemba", "Caungula", "Chitato", "Cuango", "Cuilo", "Lubalo", "Lucapa", "Xa-Muteba"],
    "Lunda Sul": ["Cacolo", "Dala", "Muconda", "Saurimo"],
    "Malanje": ["Cacuso", "Cahombo", "Calandula", "Cambundi-Catembo", "Cangandala", "Cunda-dia-Baze", "Kiuaba-N'Zoji", "Luquembo", "Malanje", "Marimba", "Massango", "Mucari", "Quela", "Quirima"],
    "Moxico": ["Camanongue", "Leua", "Luchazes", "Luena"],
    "Moxico Leste": ["Alto Zambeze", "Bundas", "Cameia (Lumeje)", "Luacano", "Luau"],
    "Namibe": ["Bibala", "Camucuio", "Namibe", "Tombwa", "Virei"],
    "Uíge": ["Ambuila", "Bembe", "Buengas", "Cangola", "Damba", "Maquela do Zombo", "Milunga", "Mucaba", "Negage", "Puri", "Quimbele", "Quitexe", "Sanza Pombo", "Songo", "Uige"],
    "Zaire": ["Cuimba", "Mbanza Congo", "N'Zeto", "Noqui", "Soyo", "Tomboco"]
}

# Correction: Bungo is in Uige. I put it in Cuanza Norte in the dict above by mistake in the thought process, but I need to verify.
# Let's check Bungo. Bungo is a municipality in Uige Province.
# Let's check Banga. Banga is a municipality in Cuanza Norte Province.
# Correcting the lists.

provinces["Uíge"].append("Bungo")
provinces["Uíge"].sort()

if "Bungo" in provinces["Cuanza Norte"]:
    provinces["Cuanza Norte"].remove("Bungo")

# Verify all municipalities are assigned
assigned_munis = []
for p in provinces:
    assigned_munis.extend(provinces[p])

missing = [m for m in municipalities if m not in assigned_munis]
duplicates = [m for m in assigned_munis if assigned_munis.count(m) > 1]

if missing:
    print(f"Missing: {missing}")
if duplicates:
    print(f"Duplicates: {set(duplicates)}")

print(json.dumps(provinces, indent=4, ensure_ascii=False))
