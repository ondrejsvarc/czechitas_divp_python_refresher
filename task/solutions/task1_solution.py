"""
Šablona pro praktický úkol 1 - Zpracování seznamu produktů.
"""


def zpracuj_produkty(seznam_produktu):
    """
    Zpracuje seznam produktů (slovníků) a vrátí celkovou hodnotu
    skladu, slovník hodnot jednotlivých naskladněných produktů a seznam produktů, které nejsou skladem.

    Args:
        seznam_produktu (list): Seznam slovníků, kde každý slovník
                                reprezentuje produkt s klíči 'name' (str),
                                'price' (float nebo int) a 'stock' (int).

    Returns:
        tuple: Trojice obsahující:
               - float: Celková hodnota všech produktů na skladě (cena * počet).
               - dict: Slovník mapující jména naskladněných produktů (str)
                       na jejich celkovou hodnotu (float). Klíč = jméno, Hodnota = cena * stock.
               - list: Seznam jmen (str) produktů, které mají stock == 0.
    """
    total_value = 0.0
    stock_product_prices = {}
    out_of_stock_products = []

    for produkt in seznam_produktu:
        name = produkt['name']
        price = produkt['price']
        stock = produkt['stock']

        # Kontrola, zda je produkt skladem
        if stock > 0:
            # Výpočet hodnoty pro tento produkt
            product_stock_value = price * stock
            # Přičtení k celkové hodnotě skladu
            total_value += product_stock_value
            # Přidání do slovníku hodnot naskladněných produktů
            stock_product_prices[name] = product_stock_value
        else:
            # Přidání jména produktu do seznamu nedostupných
            out_of_stock_products.append(name)

    return total_value, stock_product_prices, out_of_stock_products


# =============================================================================
# Blok pro spuštění a testování
# =============================================================================
if __name__ == "__main__":
    # Příklad vstupních dat
    produkty = [
        {'name': 'Laptop', 'price': 25000, 'stock': 10},
        {'name': 'Mouse', 'price': 800, 'stock': 0},
        {'name': 'Keyboard', 'price': 1200, 'stock': 5},
        {'name': 'Monitor', 'price': 6000, 'stock': 0}
    ]

    print("Zpracovávám produkty:")
    print(produkty)
    print("-" * 20)

    # Zavolání funkce
    celkova_hodnota, hodnota_jednotlivych_produktu, nejsou_skladem = zpracuj_produkty(produkty)

    # Výpis výsledků
    print(f"Celková hodnota skladu: {celkova_hodnota:.2f} Kč")

    print("Naskladněná hodnota jednotlivých produktů:")
    if hodnota_jednotlivych_produktu:
        # Seřadíme podle jména
        for nazev, hodnota in sorted(hodnota_jednotlivych_produktu.items()):
            print(f"    - {nazev}: {hodnota:.2f} Kč")
    else:
        print("    (Žádné produkty s nenulovou hodnotou skladem)")

    print("Produkty, které nejsou skladem:")
    if nejsou_skladem:
        # Seřadíme podle jména a spojíme čárkou a mezerou
        print(f"    - {', '.join(sorted(nejsou_skladem))}")
    else:
        print("    (Všechny produkty jsou skladem)")

    # Očekávaný výstup pro příklad výše:
    # Celková hodnota skladu: 256000.00 Kč
    # Naskladněná hodnota jednotlivých produktů:
    #     - Keyboard: 6000.00 Kč
    #     - Laptop: 250000.00 Kč
    # Produkty, které nejsou skladem:
    #     - Monitor, Mouse
