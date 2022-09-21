import json


def read_json(path: str) -> list[dict]:
    try:
        with open(path, "r", encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_json(path: str, new_item: dict):
    menu = read_json(path)
    id_item = len(menu) + 1

    for item in menu:
        if item["name"] == new_item["name"]:
            return "Item already exists!"

    add_new_item = {"id": id_item, **new_item}
    menu.append(add_new_item)

    with open(path, 'w') as file:
        json.dump(menu, file, indent=2)

    return add_new_item
