#!/usr/bin/python3

"""
Reading data from one format (CSV) and converting it into
another format (JSON) using serialization techniques.
"""

import csv
import json


def convert_csv_to_json(csv_filemane):
    """Converts a CSV file to a JSON file"""
    try:
        with open(csv_filemane, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False
