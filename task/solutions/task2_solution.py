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
    # 1. Načtení dat z vstupni_soubor s ošetřením chyb
    try:
        with open(vstupni_soubor, 'r', encoding='utf-8') as f:
            try:
                raw_data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Chyba: Vstupní soubor '{vstupni_soubor}' nemá validní JSON formát.")
                print(f"Detail chyby: {e}")
                return  # Ukončení funkce při nevalidním JSONu
    except FileNotFoundError:
        print(f"Chyba: Vstupní soubor '{vstupni_soubor}' nebyl nalezen.")
        return  # Ukončení funkce, pokud soubor neexistuje
    except Exception as e:  # Obecná chyba při čtení souboru
        print(f"Nastala neočekávaná chyba při čtení souboru '{vstupni_soubor}': {e}")
        return

    # Kontrola, zda načtená data jsou seznam (list)
    if not isinstance(raw_data, list):
        print(
            f"Chyba: Očekávaný formát dat ve vstupním souboru '{vstupni_soubor}' je seznam (list), nalezen {type(raw_data)}.")
        return

    # 2. Validace a čištění načtených dat
    validni_produkty = []
    print("-" * 10)
    print("Validace produktů:")
    for index, item in enumerate(raw_data):
        # Základní kontrola typu položky
        if not isinstance(item, dict):
            print(f"  - Varování: Položka na indexu {index} není slovník (dictionary), bude přeskočena: {item}")
            continue

        # Kontrola existence a typu klíčů a hodnot
        name = item.get('name')
        price = item.get('price')
        stock = item.get('stock')
        chyby_polozky = []

        if not isinstance(name, str) or not name:  # Jméno musí být neprázdný string
            chyby_polozky.append("chybějící nebo neplatné 'name' (musí být neprázdný string)")
        if not isinstance(price, (int, float)) or price < 0:  # Cena musí být číslo >= 0
            chyby_polozky.append("chybějící nebo neplatné 'price' (musí být číslo >= 0)")
        if not isinstance(stock, int) or stock < 0:  # Stock musí být celé číslo >= 0
            chyby_polozky.append("chybějící nebo neplatné 'stock' (musí být celé číslo >= 0)")

        # Pokud se vyskytly chyby, vypíšeme varování a přeskočíme položku
        if chyby_polozky:
            print(
                f"  - Varování: Položka na indexu {index} má nevalidní data ({', '.join(chyby_polozky)}), bude přeskočena: {item}")
            continue

        # Pokud je vše v pořádku, přidáme slovník do seznamu validních produktů
        validni_produkty.append({'name': name, 'price': price, 'stock': stock})
        # print(f"  - Info: Položka na indexu {index} je validní: {item}") # Lze odkomentovat pro detailní logování

    print("Validace dokončena.")
    print("-" * 10)

    # 3. Zavolání funkce pro výpočet hodnot (pouze s validními produkty)
    if not validni_produkty:
        print("Info: Nebyly nalezeny žádné validní produkty k zpracování.")
        # Můžeme se rozhodnout, zda vytvořit prázdný výstupní soubor, nebo ne. Vytvoříme ho.
        total_value = 0.0
        stock_product_prices = {}
        out_of_stock_products = []
    else:
        total_value, stock_product_prices, out_of_stock_products = zpracuj_produkty(validni_produkty)

    # 4. Příprava výsledků pro zápis do JSON
    vysledky = {
        "total_stock_value": total_value,
        "in_stock_details": stock_product_prices,
        "products_out_of_stock": sorted(out_of_stock_products)  # Seřadíme
    }
    # Seřadíme i detailní výpis
    vysledky["in_stock_details"] = dict(sorted(vysledky["in_stock_details"].items()))

    # 5. Zápis výsledků do vystupni_soubor s ošetřením chyb
    try:
        with open(vystupni_soubor, 'w', encoding='utf-8') as f:
            # ensure_ascii=False zajistí správný zápis diakritiky
            # indent=4 zajistí "hezké" formátování JSONu
            json.dump(vysledky, f, indent=4, ensure_ascii=False)
        print(f"Úspěch: Výsledky byly úspěšně uloženy do souboru '{vystupni_soubor}'.")
    except (IOError, OSError) as e:
        print(f"Chyba: Nepodařilo se zapsat výsledky do souboru '{vystupni_soubor}'.")
        print(f"Detail chyby: {e}")
    except Exception as e:  # Obecná chyba při zápisu
        print(f"Nastala neočekávaná chyba při zápisu do souboru '{vystupni_soubor}': {e}")


def zpracuj_produkty(seznam_produktu):
    """
        Zpracuje *seznam validních produktů* (slovníků) a vrátí celkovou hodnotu
        skladu, slovník hodnot jednotlivých naskladněných produktů a seznam produktů, které nejsou skladem.

        Args:
            seznam_produktu (list): Seznam slovníků, kde každý slovník
                                    reprezentuje validní produkt s klíči 'name' (str),
                                    'price' (float nebo int >= 0) a 'stock' (int >= 0).

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

    # Očekáváme, že seznam_produktu obsahuje již validované položky
    for produkt in seznam_produktu:
        name = produkt['name']
        price = produkt['price']
        stock = produkt['stock']

        # Kontrola, zda je produkt skladem (stock by měl být int >= 0)
        if stock > 0:
            product_stock_value = price * stock
            total_value += product_stock_value
            stock_product_prices[name] = product_stock_value
        else:  # stock == 0
            out_of_stock_products.append(name)

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
