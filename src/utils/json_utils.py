import json
import os


def save_data_to_file(
    data: dict, filename: str = "storage/data/analysis_data.json"
) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_data_from_file(filename: str = "storage/data/analysis_data.json") -> dict:
    if not os.path.exists(filename):
        print(f"[ERROR] File '{filename}' not found.")
        return {}
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_crypto_symbols(data):
    return [item["symbol"] for item in data.get("investment_opportunities", [])]


def update_crypto_data(data, quotes):
    for item in data.get("investment_opportunities", []):
        symbol = item.get("symbol")
        matching_quote = next((q for q in quotes if q["symbol"] == symbol), None)
        if matching_quote:
            item["price"] = round(matching_quote["price"], 2)
            item["performance"] = f"{round(matching_quote['change_7h'], 2)}%"
