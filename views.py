from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from forms import ProductForm, ProductSaleForm
from product import Product
import functions
import csv
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nini'

ITEMS = []
SOLD_ITEMS = {}

@app.route("/import_csv", methods=['GET', 'POST'])
def import_csv():
    global ITEMS 

    if request.method == 'POST':
        if 'csv_file' not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files['csv_file']
        if file.filename == '':
            flash("No selected file")
            return redirect(request.url)
        if file:
            imported_items = []
            csv_reader = csv.DictReader(file.stream.read().decode("UTF-8").splitlines())
            for row in csv_reader:
                imported_items.append(row)

            ITEMS = imported_items 
            flash("File imported successfully")
        return redirect(url_for('product_list'))
    return render_template("import_export.html")


@app.route("/export_csv", methods=['GET'])
def export_csv():
    global ITEMS

    filename = 'exported_data.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ITEMS[0].keys() if ITEMS else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in ITEMS:
            writer.writerow(item)
    flash(f'Data exported to {filename} successfully.')
    return redirect(url_for('product_list'))


@app.route("/import_export", methods=['GET'])
def import_export():
    return render_template("import_export.html")

@app.route("/products", methods = ['POST', 'GET'])
def product_list():
    form = ProductForm()

    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        unit = request.form['unit']
        unit_price = request.form['unit_price']

        for item in ITEMS:
            if item['name'] == name:
                item['quantity'] = str(int(item['quantity']) + quantity)
                break
        else:
            new_item = {"name": name, "quantity": quantity, "unit": unit, "unit_price": unit_price}
            ITEMS.append(new_item)

        return redirect(url_for("product_list"))
    
    functions.load_items_from_csv()
    return render_template("product_list.html", items=ITEMS, form=form)

@app.route('/sell/<product_name>', methods=["GET", "POST"])
def sell_product(product_name):
    form = ProductSaleForm()
    if request.method == 'POST' and form.validate_on_submit():
        quantity = int(form.quantity.data)

        for item in ITEMS:
            if item['name'] == product_name:
                item_quantity = int(item['quantity'])  # Konwersja ilości produktu na liczbę całkowitą
                if item_quantity >= quantity > 0:  # Sprawdzenie, czy ilość na stanie jest wystarczająca i czy sprzedawana ilość jest dodatnia
                    item['quantity'] = str(int(item['quantity']) - quantity)  # Konwersja wyniku odejmowania na string
                    if item['name'] in SOLD_ITEMS:
                        SOLD_ITEMS[item['name']]['quantity'] += quantity
                    else:
                        SOLD_ITEMS[item['name']] = {'quantity': quantity, 'unit_price': item['unit_price']}
                elif quantity <= 0:
                    flash("Ilość musi być dodatnia.")
                else:
                    flash("Nie masz wystarczającej ilości tego produktu.")
                break
        return redirect(url_for('product_list'))
    return render_template("sell_product.html", form=form, product_name=product_name)



@app.route("/revenue", methods=['GET'])
def sell_product_list():
    return render_template("revenue.html", sold_items=SOLD_ITEMS, items=ITEMS)

@app.context_processor
def inject_active():
    active = request.path  # Pobierz bieżący URL
    return dict(active=active)

@app.route("/")
def homepage():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)