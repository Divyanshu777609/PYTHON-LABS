import json

logs = [
    {"level": "INFO", "message": "Program started"},
    {"level": "ERROR", "message": "File not found"},
    {"level": "INFO", "message": "User logged in"},
    {"level": "WARNING", "message": "Low disk space"},
    {"level": "ERROR", "message": "Connection failed"}
]

with open("logs.json", "w") as file:
    json.dump(logs, file, indent=4)

with open("logs.json", "r") as file:
    data = json.load(file)

counts = {}

for entry in data:
    level = entry["level"]

    counts[level] = counts.get(level, 0) + 1

print("Log summary:")

for level, count in counts.items():
    print(level, ":", count)