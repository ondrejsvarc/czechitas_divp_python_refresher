"""
Šablona pro praktický úkol 2 - Zpracování produktů z JSON souboru.
"""

import json


def zpracuj_produkty_ze_souboru(vstupni_soubor, vystupni_soubor):
    """
    Načte seznam produktů z JSON souboru, zpracuje je s ošetřením chyb
    a uloží výsledek (celkovou hodnotu skladu, hodnota naskladněných
    produktů a seznam produktů mimo sklad) do jiného JSON souboru.

    Args:
        vstupni_soubor (str): Cesta k vstupnímu JSON souboru.
                               Soubor by měl obsahovat seznam slovníků.
        vystupni_soubor (str): Cesta k výstupnímu JSON souboru, kam se
                               uloží výsledky.
    """
    # TODO: Implementuj logiku funkce zde.
    # 1. Načtení dat z vstupni_soubor:
    #    - Použij blok try-except pro FileNotFoundError a json.JSONDecodeError.
    #    - Pokud nastane chyba, vypiš informativní hlášku a ukonči funkci (return).
    # 2. Zpracování načtených dat:
    #    - Převeď data na správné typy (možná vytvoření objektů pro produkty?)
    #    - Vynech chybná dat a vypiš informativní hlášky.
    # 3. Zavolání funkce zpracuj_produkty() (možná na vstupu seznam objektů?)
    # 4. Zápis výsledků do vystupni_soubor:
    #    - Použij blok try-except pro případné chyby při zápisu (IOError/OSError).
    #    - Použij json.dump() s argumentem indent=4 pro hezké formátování.
    #    - Vypište informaci o úspěšném uložení nebo chybě.

    data = None     # Sem načti data ze souboru

    # Zde implementujte načítání a zpracování...
    pass

    total_value, stock_product_prices, out_of_stock_products = zpracuj_produkty()

    # Až budeš mít výsledky, připrav slovník pro zápis
    vysledky = {
        "total_stock_value": total_value,
        "in_stock_details": stock_product_prices,
        "products_out_of_stock": out_of_stock_products
    }

    # Zde implementuj zápis do souboru...
    pass


def zpracuj_produkty():
    # ToDo: Zde implementuj upravenou funkci z prvního úkolu

    total_value = 0.0
    stock_product_prices = {}
    out_of_stock_products = []

    pass

    return total_value, stock_product_prices, out_of_stock_products


# =============================================================================
# Blok pro spuštění a testování
# =============================================================================
if __name__ == "__main__":
    # Definice názvů souborů pro testování
    TEST_INPUT_FILENAME = "test_input.json"
    TEST_OUTPUT_FILENAME = "test_output.json"

    print("-" * 20)
    print(f"Spouštím zpracování z '{TEST_INPUT_FILENAME}' do '{TEST_OUTPUT_FILENAME}'...")
    print("-" * 20)

    # Zavolání funkce
    zpracuj_produkty_ze_souboru(TEST_INPUT_FILENAME, TEST_OUTPUT_FILENAME)

    print("-" * 20)
    print("Zpracování dokončeno.")
