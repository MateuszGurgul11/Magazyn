items = [
    {'name' : 'Komputer', 'quantity' : 2, 'unit' : 'kg', 'unit_price' : 1300},
    {'name' : 'Drukarka', 'quantity' : 3, 'unit' : 'kg', 'unit_price': 1000},
    {'name' : 'Mikrofala', 'quantity' : 1, 'unit' : 'kg', 'unit_price': 500}
]

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
    sell_name = input("Podaj nazwe przedmiotu: ")
    sell_name = sell_name.capitalize()
    sell_quantity = int(input("Podaj ilosc jaka chcesz kupic: "))

    for item in items:
        if sell_name == item['name']:
            price = item['unit_price'] * sell_quantity
            item['quantity'] -= sell_quantity

            new_dict = {'name' : sell_name, 'quantity' : sell_quantity, 'unit_price' : price}
            sold_items.append(new_dict)

            if item['quantity'] == 0:
                print('Produkt jest wyprzedany')
                item['quantity'] = 0

    get_items()
    print(f"Sprzedano {sell_name} ilosc sztuk: {sell_quantity} o wartosci {price}")

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
    elif menu_answer.lower() == 'exit':
        print("Wychodzisz z programu!")
        exit()

while True:
    menu()
