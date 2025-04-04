import json
import os


def save_data_to_file(data: dict, filename: str = "analysis_data.json") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_data_from_file(filename: str = "analysis_data.json") -> dict:
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return {}
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
