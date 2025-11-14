#!/usr/bin/python3
"""
Flask application that reads product data from JSON or CSV files
and displays them using Jinja2 templates.
"""
from flask import Flask, request, render_template
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    items_list = data['items']
    print("Items récupérés:", items_list)
    return render_template('items.html', items=items_list)


def read_json(filename):
    """Read and parse data from JSON file."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            # Gère les deux formats possibles
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and 'products' in data:
                return data['products']
            else:
                return None
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def read_csv(filename):
    """Read and parse data from CSV file."""
    try:
        product_list = []
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                product_list.append(product)
        return product_list
    except (FileNotFoundError, ValueError, KeyError):
        return None


@app.route('/products')
def product_list():
    """Route to display products from JSON or CSV file."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Valider le paramètre source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Lire les données selon la source
    if source == 'json':
        products = read_json('products.json')
    else:
        products = read_csv('products.csv')

    # Gérer les erreurs de lecture
    if products is None:
        return render_template(
            'product_display.html',
            error=f"Error reading {source.upper()} file"
            )

    # Filtrer par ID si fourni
    if product_id:
        try:
            product_id = int(product_id)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                return render_template(
                    'product_display.html',
                    error="Product not found"
                    )
        except ValueError:
            return render_template(
                'product_display.html',
                error="Invalid product ID"
                )

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
