#Mějme zadaný následující seznam naměřených teplot. 
#Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
#Vytvořte seznam průměrných teplot pro každý den.
#Vytvořte seznam ranních teplot.
#Vytvořte seznam nočních teplot.
#Vytvořte seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.

prumer = [round(sum(teplota) / len(teplota)) for teplota in teploty]
print(prumer)

ranni_teploty = [den[0] for den in teploty]
print(ranni_teploty)
nocni_teploty = [noc[3] for noc in teploty]
print(nocni_teploty)
seznam = [[den[1], den[3]] for den in teploty]
print(seznam)