jmeno = "Kristýna"
domena = "@czechitas.cz"
print(jmeno + domena)



#bonus úkolu, ale nedodělaný, nevěděla jsem jak udělat standartní variantu jména nebo jak vložit tečky za iniciály

jmeno = input("Napište prosím své jméno: ")
prijmeni = input("Napište prosím své příjmení: ")
jmeno_a_prijmeni = (jmeno) + (" ") + prijmeni
print (jmeno_a_prijmeni.upper())
print (jmeno_a_prijmeni.lower())
inicialy = jmeno[0] + prijmeni[0]
print(inicialy.upper())
