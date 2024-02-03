items = [
    {'name' : 'Komputer', 'quantity' : 2, 'unit' : 'kg', 'unit_price' : 1300},
    {'name' : 'Drukarka', 'quantity' : 3, 'unit' : 'kg', 'unit_price': 1000},
    {'name' : 'Mikrofala', 'quantity' : 1, 'unit' : 'kg', 'unit_price': 500}
]

def get_items():
    title = "Name\tQuantity\tUnit\tUnit Price (PLN)\t \n"
    title += "----\t-----------\t----\t----------------"
    print(title)
    for item in items:
        item_title = f"{item['name']}\t"
        item_title += f"{item['quantity']}\t"
        item_title += f"{item['unit']}\t"
        item_title += f"{item['unit_price']}\t"
        print(item_title)


def add_items():
    name = input("Nazwa przedmiotu: ")
    name = name.capitalize()
    unit_name = input("Podaj jednostke: ")
    quantity = int(input("Podaj ilosc: "))
    unit_price = int(input("Podaj cene towaru: "))

    new_dict = {'name' : name, 'quantity' : quantity, 'unit' : unit_name, 'unit_price' : unit_price}
    items.append(new_dict)

    get_items()

def menu():
    menu_answer = input("Co chcialbys zrobic? ")

    if menu_answer.lower() == 'magazyn':
        get_items()
    elif menu_answer.lower() == 'dodaj':
        add_items()
    elif menu_answer.lower() == 'exit':
        print("Wychodzisz z programu!")
        exit()

while True:
    menu()
