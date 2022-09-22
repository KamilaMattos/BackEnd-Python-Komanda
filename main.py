from utils.json_handler import write_json
from management.tab_handler import calculate_tab


def main():
    new_item = {"name": "CHURROS DO M5", "price": 5.0}
    write_json('menu.json', new_item)

    table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
    table_2 = [
        {"id": 10, "amount": 3},
        {"id": 20, "amount": 2},
        {"id": 21, "amount": 5},
    ]

    # return calculate_tab('menu.json', table_1)
    return calculate_tab('menu.json', table_2)


if __name__ == "__main__":
    print(main())
