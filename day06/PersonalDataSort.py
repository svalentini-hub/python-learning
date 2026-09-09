# Personal made data sort
print("Welcome to League of Legends champion sorting!")

champions = [
    {"Name": "Yasuo", "class": "fighter", "difficulty rating": 7.5},
    {"Name": "Yone", "class": "fighter", "difficulty rating": 9},
    {"Name": "Gangplank", "class": "bruiser", "difficulty rating": 10},
    {"Name": "Garen", "class": "fighter", "difficulty rating": 2},
    {"Name": "Ryze", "class": "Mage", "difficulty rating": 8},
    {"Name": "Kha'Zix", "class": "Assassin", "difficulty rating": 6.5},
    {"Name": "Millio", "class": "Support", "difficulty rating": 2}

]


filtered_champions = [champs for champs in champions if champs["class"] == "fighter"]
print(filtered_champions)
hard_champions = [champs for champs in filtered_champions if champs["difficulty rating"] > 2]

print(hard_champions)