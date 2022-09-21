from utils.json_handler import read_json, write_json


if __name__ == "__main__":
    # print(read_json('menu.json'))
    new_item = {"name": "CHURROS DO M5", "price": 5.0}
    print(write_json('menu.json', new_item))
