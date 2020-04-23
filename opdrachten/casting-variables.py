prijsPrei = 2
print("Prei kost"+ str(prijsPrei) + " euro per kilo")


bestelling = "prei 4"

totaalPrijs = int(bestelling[bestelling.find(" ") + 1 :]) * prijsPrei
print(totaalPrijs)

broccoliPrijs = 2.34
bestellingBroccoli = "broccoli 1.6"
bestellingBroccoliKG = bestellingBroccoli[bestellingBroccoli.find(' '):]
broccoliTotaalPrijs = float(
    bestellingBroccoliKG)*broccoliPrijs

print(bestellingBroccoliKG + " kilo broccoli kost " +
      str(round(broccoliTotaalPrijs, 2)) + " euro")