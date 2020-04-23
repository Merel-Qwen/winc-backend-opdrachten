# spelers
hans = "Hans van Breukelen"
berry = "Berry van Aerle"
ronald = "Ronald Koeman"
adri = "Adri van Tiggelen"
gerald = 'Gerald Vanenburg'
arnold = 'Arnold Mühren'
jan = 'Jan Wouters'
erwin = "Erwin Koeman"
marco = "Marco van Basten"
ruud = "Ruud Gullit"

# doelpunten
eersteDoelPunt = 35
tweedeDoelPunt = 54
print(ruud + " scoorde in de ", eersteDoelPunt,
      "e minuut." + "\n" + marco + "scoorde in", tweedeDoelPunt, "e minuut.")

# deel 2

Voornaam = marco[0: marco.find(" ")]
print(Voornaam)

lengteMarco = len(marco)
print(lengteMarco)
VBM = marco[6:] + " " +marco[:6]
print(VBM)


VoorletterEnAchternaam = marco[0: 1] + ". " + marco[marco.find(" ")+1:]
print(VoorletterEnAchternaam)

vierKeerMarco = (len(marco[0:marco.find(" ")]) *
                    (marco[0:marco.find(" ")]+"! ")).strip(" ")

print(vierKeerMarco)





