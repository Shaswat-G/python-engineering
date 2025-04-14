"""
Complete Python Demo: File Handling & SQLite Database Operations
This script demonstrates how to handle CSV, JSON, XML, YAML, Excel, ZIP files, and SQLite databases.
"""

import csv
import json
import yaml
import zipfile
import pandas as pd
import sqlite3
import xml.etree.ElementTree as ET
from openpyxl import Workbook


# --- CSV Handling ---
def handle_csv():
    data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
    with open("people.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    with open("people.csv", "r") as f:
        reader = csv.reader(f)
        print("\nCSV Data:")
        for row in reader:
            print(row)


# --- JSON Handling ---
def handle_json():
    data = {"name": "Alice", "age": 30, "city": "London"}
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    with open("data.json", "r") as f:
        loaded = json.load(f)
        print("\nJSON Data:", loaded)


# --- YAML Handling ---
def handle_yaml():
    config = {"app": "demo", "version": 1.0, "features": ["a", "b"]}
    with open("config.yml", "w") as f:
        yaml.dump(config, f)

    with open("config.yml", "r") as f:
        loaded = yaml.safe_load(f)
        print("\nYAML Config:", loaded)


# --- XML Handling ---
def handle_xml():
    root = ET.Element("People")
    person = ET.SubElement(root, "Person")
    ET.SubElement(person, "Name").text = "Alice"
    ET.SubElement(person, "Age").text = "30"
    tree = ET.ElementTree(root)
    tree.write("people.xml")

    tree = ET.parse("people.xml")
    root = tree.getroot()
    print("\nXML Data:")
    for p in root.findall("Person"):
        print(p.find("Name").text, p.find("Age").text)


# --- Excel Handling ---
def handle_excel():
    df = pd.DataFrame([{"Name": "Alice", "Age": 30}, {"Name": "Bob", "Age": 25}])
    df.to_excel("people.xlsx", index=False)
    loaded_df = pd.read_excel("people.xlsx")
    print("\nExcel Data:\n", loaded_df)


# --- ZIP Handling ---
def handle_zip():
    with zipfile.ZipFile("archive.zip", "w") as zipf:
        zipf.write("people.csv")
        zipf.write("data.json")

    with zipfile.ZipFile("archive.zip", "r") as zipf:
        print("\nZIP Contents:", zipf.namelist())
        zipf.extractall("unzipped_files")


# --- SQLite Handling ---
def handle_sqlite():
    movies = [
        {"id": 1, "title": "Inception", "year": 2010},
        {"id": 2, "title": "Interstellar", "year": 2014},
    ]

    with sqlite3.connect("demo.db") as conn:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS Movies (id INTEGER, title TEXT, year INTEGER)"""
        )
        conn.executemany(
            "INSERT OR REPLACE INTO Movies VALUES (?, ?, ?)",
            [tuple(m.values()) for m in movies],
        )
        conn.commit()
        cursor = conn.execute("SELECT * FROM Movies")
        print("\nSQLite Data:")
        for row in cursor.fetchall():
            print(row)


# --- Run All ---
if __name__ == "__main__":
    handle_csv()
    handle_json()
    handle_yaml()
    handle_xml()
    handle_excel()
    handle_zip()
    handle_sqlite()
