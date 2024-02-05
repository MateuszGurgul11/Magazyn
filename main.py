import csv


items = []
sold_items = []

def get_items():
    title = "Nazwa\t \tIlość\tJednostki\tCena (PLN)\t \n"
    title += "----\t \t------\t---------\t----------------"
    print(title)
    for item in items:
        item_title = f"{item['name']}\t"
        item_title += f"{item['quantity']}\t"
        item_title += f"{item['unit']}\t \t"
        item_title += f"{item['unit_price']}\t"
        print(item_title)


def add_items():
    name = input("Nazwa przedmiotu: ")
    name = name.capitalize()
    unit_name = input("Podaj jednostkę: ")
    quantity = int(input("Podaj ilość: "))
    unit_price = int(input("Podaj cenę towaru: "))

    item_exists = False

    for item in items:
        if name == item['name']:
            item['quantity'] += quantity
            item['unit_price'] += unit_price
            item_exists = True

    if not item_exists:
        new_dict = {'name': name, 'quantity': quantity, 'unit': unit_name, 'unit_price': unit_price}
        items.append(new_dict)

    get_items()


def sell_items():
    sell_name = input("Podaj nazwę przedmiotu: ")
    sell_name = sell_name.capitalize()
    sell_quantity = int(input("Podaj ilość, sprzedanych przedmiotów: "))

    item_found = False 

    for item in items:
        if sell_name == item['name']:
            if sell_quantity <= item['quantity']:
                price = item['unit_price'] * sell_quantity
                item['quantity'] -= sell_quantity

                new_dict = {'name': sell_name, 'quantity': sell_quantity, 'unit_price': price}
                sold_items.append(new_dict)

                print(f"Sprzedano {sell_name} ilość sztuk: {sell_quantity} o wartości {price}")
            else:
                print("-------------------------------------------------")
                print(f"Niewystarczająca ilość {sell_name} w magazynie.")
                print("-------------------------------------------------")
            item_found = True
            break

    if not item_found:
        print(f"Przedmiot {sell_name} nie znajduje się w magazynie.")

    get_items()


def get_cost():
    costs = sum(price['unit_price'] for price in items)
    return costs

def get_income():
    income = sum(price['unit_price'] for price in sold_items)
    return income

def show_revenue():
    total_cost = get_cost()
    total_income = get_income()
    total_revanue = total_income - total_cost

    revenue = "Przychody (PLN) \n"
    revenue += f"Dochód: {total_income} \n"
    revenue += '----------------- \n'
    revenue += f"Przychody {total_revanue} PLN"

    print(revenue)


def export_items_to_csv():
    with open('magazyn.csv', 'w', newline = '') as csvfile:
        filednames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames = filednames)

        writer.writeheader()

        for item in items:
            writer.writerow(item)

        print('Dane magazynu zostaly wyeksportowane prawidlowo!')

def export_sales_to_csv():
    with open('sold_items.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'quantity', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in sold_items:
            writer.writerow(item)

    print('Dane sprzedaży zostały wyeksportowane prawidłowo!')


def load_items_from_csv(file_path):
    global items
    items.clear()

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append(row)

    print(f"Dane z pliku {file_path} zostały wczytane")



def menu():
    menu_answer = input("Co chcialbys zrobic? ")

    if menu_answer.lower() == 'storage':
        get_items()
    elif menu_answer.lower() == 'add':
        add_items()
    elif menu_answer.lower() == 'sell':
        sell_items()
    elif menu_answer.lower() == 'revenue':
        show_revenue()
    elif menu_answer.lower() == 'save':
        export_items_to_csv()
        export_sales_to_csv()
    elif menu_answer.lower() == 'load':
        file_path = input("Podaj ścieżkę do pliku CSV: ")
        load_items_from_csv(file_path)
    elif menu_answer.lower() == 'exit':
        print("Wychodzisz z programu!")
        exit()


def main():
    file_path = input("Podaj ściezkę do pliku magazynu (CSV): ")

    try:
        load_items_from_csv(file_path)
    except FileNotFoundError:
        print(f"Plik o ściezce {file_path} nie został znaleziony. Dane magazynu zostaną wczytane z domyślnej listy")
    while True:
        menu()


if __name__ == "__main__":
    main()