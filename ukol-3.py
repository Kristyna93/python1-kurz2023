import json

file_path = "body.json"

with open("Lekce03/body.json", mode="r", encoding="utf-8") as soubor:
    body = json.load(soubor)
print(body)

novy_slovnik = {}
i=0
for key, value in body.items():
    if value < 60:
        hodnoceni = "Fail"
    else:
        hodnoceni = "Pass"
    #print(key, ":", hodnoceni)
    novy_slovnik[i] = {key : hodnoceni}
    i += 1

print (novy_slovnik)
with open("Lekce03/prospech.json", mode="w", encoding="utf-8") as soubor:
    json.dump(novy_slovnik, soubor, ensure_ascii=False)