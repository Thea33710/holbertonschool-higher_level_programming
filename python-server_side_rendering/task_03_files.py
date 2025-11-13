from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# -------- Helper functions --------
def read_json_file():
    """Reads product data from JSON file."""
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
        return data
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


# -------- Routes --------
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    products_data = []
    error_message = None

    if source == "json":
        products_data = read_json_file()
    elif source == "csv":
        products_data = read_csv_file()
    else:
        error_message = "Wrong source. Please use ?source=json or ?source=csv."
        return render_template('product_display.html', error=error_message)

    if products_data is None:
        error_message = "Error reading data file."
        return render_template('product_display.html', error=error_message)

    if product_id is not None:
        products_data = [p for p in products_data if p["id"] == product_id]
        if not products_data:
            error_message = f"Product with id {product_id} not found."
            return render_template('product_display.html', error=error_message)

    return render_template('product_display.html', products=products_data, source=source)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
