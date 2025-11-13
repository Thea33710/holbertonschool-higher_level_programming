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
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and 'products' in data:
                return data['products']
            else:
                return None
    except Exception:
        return None


def read_csv_file():
    """Reads product data from CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception:
        return None


def read_sqlite_data(product_id=None):
    """Reads product data from SQLite database."""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()

        products = []

        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)

        conn.close()

        return products
    except Exception:
        return None


# ---------- Routes ----------

@app.route('/products')
def products():
    """
    Route to display products from JSON, CSV file, or SQLite database.
    """
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    products_data = []
    error_message = None

    # Choix de la source
    if source == "json":
        products_data = read_json_file()
    elif source == "csv":
        products_data = read_csv_file()
    elif source == "sql":
        products_data = read_sqlite_data(product_id)
    else:
        error_message = (
            "Wrong source. Please use ?source=json,"
            " ?source=csv, or ?source=sql."
        )
        return render_template('product_display.html', error=error_message)

    # Gestion d’erreurs de lecture
    if products_data is None:
        error_message = "Error reading data from the selected source."
        return render_template('product_display.html', error=error_message)

    # Filtrage (pour JSON et CSV)
    if source in ["json", "csv"] and product_id is not None:
        products_data = [p for p in products_data if p["id"] == product_id]

    # Aucun produit trouvé
    if not products_data:
        error_message = (
            f"Product with id {product_id} not found."
            if product_id
            else "No products found."
        )
        return render_template('product_display.html', error=error_message)

    # Sinon, on affiche les données
    return render_template(
        'product_display.html',
        products=products_data,
        source=source
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
