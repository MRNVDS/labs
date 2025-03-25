import json
import jsonschema
from jsonschema import validate

with open("_1_invalid.json", encoding="utf-8") as f:
    data = json.load(f)

with open("schema_1.json", encoding="utf-8") as f:
    schema = json.load(f)

try:
    validate(instance=data, schema=schema)
    print("JSON корректен и прошёл валидацию.")
except jsonschema.exceptions.ValidationError as e:
    print("Валидация не пройдена:")
    print(e)
