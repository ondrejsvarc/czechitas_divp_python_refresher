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
    # ToDo: Implementuj logiku funkce zde.
    # - Inicializuj proměnné pro celkovou hodnotu a seznam produktů mimo sklad.
    # - Projdi cyklem 'seznam_produktu'.
    # - Pro každý produkt přičti jeho hodnotu (cena * stock) k celkové hodnotě.
    # - Pokud je stock produktu 0, přidej jeho 'name' do seznamu produktů mimo sklad.
    # - Pokud není stock produktu 0, přidej jeho hodnotu (cena * stock) do slovníku naskladněných produktů (key=name)
    # - Na konci vrať vypočítanou celkovou hodnotu, slovník cen a seznam jmen.

    total_value = 0.0
    stock_product_prices = {}
    out_of_stock_products = []

    # Příklad: Nahraď 'pass' svou implementací
    pass

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
    # ToDo: Implementuj výpis řešení zde, jednotlivé produkty seřaď dle jména (v seznamu i slovníku)

    # Očekávaný výstup pro příklad výše:
    # Celková hodnota skladu: 256000.00 Kč
    # Naskladněná hodnota jednotlivých produktů:
    #     - Keyboard: 6000.00 Kč
    #     - Laptop: 250000.00 Kč
    # Produkty, které nejsou skladem:
    #     - Monitor, Mouse
