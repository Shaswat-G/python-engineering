"""
Python Utilities Demo Script
Demonstrates usage of time, randomness, templating, configs, and subprocess.

Run As : python script.py --config config.json --epochs 10
"""

import time
from datetime import datetime, timedelta
import random
import numpy as np
import pandas as pd
import torch
from string import Template
import json
import xml.etree.ElementTree as ET
import argparse
import subprocess


# --- Time Handling ---
def time_demo():
    print("\n--- Time Demo ---")
    print("Current timestamp:", time.time())
    print("Current datetime:", datetime.now())

    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter()
    print(f"Elapsed (sleep): {end - start:.4f} sec")

    dt = datetime.now() + timedelta(days=5)
    print("+5 days:", dt.strftime("%Y-%m-%d"))


# --- Randomness ---
def randomness_demo():
    print("\n--- Randomness Demo ---")
    random.seed(42)
    np.random.seed(42)
    torch.manual_seed(42)

    print("Random int:", random.randint(1, 10))
    print("Random choice:", random.choice(["apple", "banana", "cherry"]))

    nums = list(range(5))
    random.shuffle(nums)
    print("Shuffled:", nums)

    print("Numpy random:", np.random.rand(2, 2))
    print("Torch random:", torch.rand(2, 2))

    # Monte Carlo estimate of π
    inside = 0
    total = 10000
    for _ in range(total):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
    print("Estimated π:", 4 * inside / total)


# --- Templating ---
def templating_demo():
    print("\n--- Templating Demo ---")
    template = Template("Hello $name, your order #$order has shipped.")
    print(template.substitute({"name": "Alice", "order": "12345"}))


# --- Config Handling ---
def config_demo(json_path="config.json", xml_path="config.xml"):
    print("\n--- Config Demo ---")

    # JSON
    config_data = {"version": 1.0, "debug": True}
    with open(json_path, "w") as f:
        json.dump(config_data, f)

    with open(json_path, "r") as f:
        config = json.load(f)
    print("JSON Config:", config)

    # XML
    root = ET.Element("settings")
    ET.SubElement(root, "version").text = "1.0"
    ET.SubElement(root, "debug").text = "true"
    tree = ET.ElementTree(root)
    tree.write(xml_path)

    tree = ET.parse(xml_path)
    for child in tree.getroot():
        print(f"{child.tag}: {child.text}")


# --- Argparse Demo ---
def argparse_demo():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config", type=str, help="Path to config file", default="config.json"
    )
    parser.add_argument("--epochs", type=int, default=5)
    args = parser.parse_args()

    print("\n--- Argparse Demo ---")
    print("Epochs:", args.epochs)
    with open(args.config) as f:
        cfg = json.load(f)
        print("Loaded config:", cfg)


# --- Subprocess Demo ---
def subprocess_demo():
    print("\n--- Subprocess Demo ---")
    result = subprocess.run(
        ["echo", "Hello from subprocess"], capture_output=True, text=True
    )
    print("STDOUT:", result.stdout.strip())
    print("Exit Code:", result.returncode)


# --- Main ---
if __name__ == "__main__":
    time_demo()
    randomness_demo()
    templating_demo()
    config_demo()
    subprocess_demo()

    # For argparse_demo() - run as a separate script from CLI to see arg parsing in action
