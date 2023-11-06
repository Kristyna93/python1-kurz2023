class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.reregistracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"
    def get_info(self):
        return f"Auto s registrační značkou {self.reregistracni_znacka} má značku a typ vozidla {self.typ_vozidla}."


auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

pujceni = input("Napište značku auta, kterou si chcete půjčit, buď Skoda nebo Peugeot: ")    
if pujceni == "Peugeot":
    vysledek = auto1
elif pujceni == "Skoda":
    vysledek = auto2
else:
    print("Takové auto nemáme")

print(vysledek.get_info())
print(vysledek.pujc_auto())
print(vysledek.pujc_auto()) #auto již není možné půjčit podruhé