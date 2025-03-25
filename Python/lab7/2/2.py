import json

with open("_2.json", encoding="utf-8") as f:
    users = json.load(f)

result = {user["username"]: user["phone"] for user in users}
print(result)