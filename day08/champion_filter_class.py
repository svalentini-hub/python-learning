import json
import csv
import os

class ChampionFilter:
    def __init__(self, json_path, csv_path):
        self.json_path = json_path
        self.csv_path = csv_path
        self.data = []
        self.filtered = []

    def load_data(self):
        try:
            with open(self.json_path, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print("The selected file does not exist")
            exit()
        except json.JSONDecodeError:
            print("The JSON file contains an error, fix it")
            exit()

    def filter_champions(self, min_pick_rate):
       self.filtered = [champ for champ in self.data if champ["pick_rate"] > min_pick_rate]


    def write_csv(self):
        with open(self.csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "role", "release_year", "pick_rate"])
            writer.writeheader()
            writer.writerows(self.filtered)



script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "LeagueChamps2.json")
csv_path = os.path.join(script_dir, "FilteredChampions2.csv")

filterer = ChampionFilter(json_path, csv_path)
filterer.load_data()
filterer.filter_champions(10)
filterer.write_csv()