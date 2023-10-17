import json

file_path = "body.json"

with open("Lekce03/body.json", mode="r", encoding="utf-8") as soubor:
    body = json.load(soubor)
print(body)

novy_slovnik = {}

for key, value in body.items():
    if value >= 60:
        novy_slovnik[key] = "Pass"
    else:
        novy_slovnik[key] = "Fail"
   
print (novy_slovnik)
with open("Lekce03/prospech.json", mode="w", encoding="utf-8") as soubor:
    json.dump(novy_slovnik, soubor, ensure_ascii=False)