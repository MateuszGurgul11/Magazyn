import csv
from flask import flash

def load_items_from_csv():
    global ITEMS
    ITEMS = []

    try:
        with open('exported_data.csv', newline='') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                ITEMS.append(row)
    except FileNotFoundError:
        flash("File not found")