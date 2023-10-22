def overeni(cislo):
    if len(cislo) == 9:
        if cislo.isdigit():
            return True
    elif len(cislo) == 13:
        if cislo.startswith("+420") and cislo[4:].isdigit():
            return True
    return False

def cena_sms(zprava):
    znaky = len(zprava)
    cena = znaky // 180 * 3
    if znaky % 180 != 0:
        cena += 3
    return cena

cislo = input("Napište telefonní číslo příjemce: ")
if not overeni(cislo):
    print("Chybný formát.")
else:
    zprava = input("Napiš text zprávy: ")
    cena = cena_sms (zprava)
    print("Celkem za zprávu zaplatíte", cena, "Kč.")