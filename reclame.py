def aanbieding_1 (smaak, prijs, korting):
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {korting} euro."
def inkomsten_totaal (inkomsten):
    totaal = 0
    for x in inkomsten:
        totaal += x
    return totaal