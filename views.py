from flask import Flask, render_template, request, url_for, redirect
import main
from forms import ProductForm
from product import Product

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nini'

ITEMS = [
    Product("Mleko", "litr", 2.5, 100),
    Product("Chleb", "sztuka", 2.0, 50),
    Product("Jajka", "sztuka", 0.5, 200),
]

@app.route("/products", methods = ['POST', 'GET'])
def product_list():
    form = ProductForm()

    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        unit = request.form['unit']
        unit_price = request.form['unit_price']

        new_item = Product(name, quantity, unit, unit_price)
        ITEMS.append(new_item)
        return redirect(url_for("product_list"))
    return render_template("product_list.html", items=ITEMS, form=form)

@app.route("/")
def homepage():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)