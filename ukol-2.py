sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Vložte prosím kód součástky: ")
if not kod_soucastky in sklad:
  print("Soucastku nemame skladem.")
elif kod_soucastky in sklad:
    mnozstvi = int(input("Napište množství součástek: "))
    if (mnozstvi > sklad[kod_soucastky]):
        print("Lze prodat jen omezene mnozstvi.")
        sklad.pop(kod_soucastky)
        print(sklad)
    elif (mnozstvi <= sklad[kod_soucastky]):
        print("Poptávku lze uspokojit v plné výši.")
        sklad[kod_soucastky] -= mnozstvi
        print(sklad)