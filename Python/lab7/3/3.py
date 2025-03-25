import json

with open("_3.json", encoding="utf-8") as f:
    data = json.load(f)

new_item = {
    "id": 2,
    "name": "Smartphone",
    "price": 30000
}

data["Inv"].append(new_item)

with open("updated_3.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Объект добавлен и сохранён в updated_3.json")
