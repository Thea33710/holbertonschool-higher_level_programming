from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# ---------- Helper functions ----------
def read_json_file():
    """Reads product data from JSON file."""
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
        return data
    except Exception:
        return []


def read_csv_file():
    """Reads product data from CSV file."""
    products = []
    try:
        with open('products.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception:
        pass
    return products


def read_sqlite_data(product_id=None):
    """Reads product data from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except Exception:
        products = None
    return products



# ---------- Routes ----------

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id', type=int)
    error = None

    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    elif source == 'sql':
        products = read_sqlite_db()
        if products is None:
            error = "Database error"
            products = []
    else:
        products = []
        error = "Wrong source"

    if id_param is not None:
        filtered = [p for p in products if p['id'] == id_param]
        if filtered:
            products = filtered
        else:
            products = []
            error = "Product not found"

    return render_template('product_display.html', products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
