print("Hello, welcome to the user records filter, please change the below dictionaries with the desired values!")

users = [
    {"name": "Ana", "age": 25, "city": "Bucharest"},
    {"name": "Alex", "age": 31, "city": "Carei"},
    {"name": "Dan", "age": 18, "city": "Brasov"},
    {"name": "Stefan", "age": 29, "city": "Bucharest"},
    {"name": "Victor", "age": 30, "city": "Bucharest"},
    {"name": "Daria", "age": 26, "city": "Bucharest"}

]


# users older than 24 in Bucharest
for user in users:
    if user["age"] > 24 and user["city"] == "Bucharest":
        print(user)

# sort by age
older_users = [user for user in users if user["age"] > 24]
sorted_older_users = sorted(older_users, key=lambda user: user["age"])
print(sorted_older_users)

#just names

names = [user["name"] for user in users]
print(names)