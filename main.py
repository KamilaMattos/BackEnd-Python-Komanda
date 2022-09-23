from utils.json_handler import write_json
from management.tab_handler import calculate_tab

FILEPATH = 'menu.json'
TABLE_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
new_item = {"name": "CHURROS DO M5", "price": 5.0}


def main():

    # return write_json(FILEPATH, new_item)
    return calculate_tab(TABLE_1)


if __name__ == "__main__":
    print(main())
