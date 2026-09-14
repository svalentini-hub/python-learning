import os
import json
import csv
from champion_filter_class import ChampionFilter

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "LeagueChamps2.json")
csv_path = os.path.join(script_dir, "FilteredChampions2.csv")

filterer = ChampionFilter(json_path, csv_path)
filterer.load_data()
filterer.filter_champions(10)
filterer.write_csv()