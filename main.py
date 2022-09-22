from utils.json_handler import write_json
from management.tab_handler import calculate_tab

FILEPATH = 'menu.json'


def main():
    new_item = {"name": "CHURROS DO M5", "price": 5.0}
    write_json('menu.json', new_item)

    TABLE_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]

    return calculate_tab(TABLE_1, FILEPATH)


if __name__ == "__main__":
    print(main())
