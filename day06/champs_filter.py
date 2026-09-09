# Self made filter for champions
import json
import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "LeagueChamps.json")
csv_path = os.path.join(script_dir, "filtered_champions.csv")


try:
    with open(json_path, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: Leaguechamps.json not found. ")
    exit()
except json.JSONDecodeError:
    print("Error: LeagueChamps.json is not valid JSON. ")
    exit()
filtered_champions = [c for c in data if c["pick_rate"] > 10]

with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "role", "release_year", "pick_rate"])
    writer.writeheader()
    writer.writerows(filtered_champions)



