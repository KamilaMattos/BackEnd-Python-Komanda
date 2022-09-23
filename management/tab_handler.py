from datetime import datetime
from utils.json_handler import read_json


def get_item_menu(filepath: str, id_item_table: int):
    menu = read_json(filepath)

    for items in menu:
        if items['id'] == id_item_table:
            return items


def calculate_tab(table: list[dict]) -> dict:
    filepath = 'menu.json'
    date_time = '11/10/2011 12:00:00'
    subtotal = 0

    for items in table:
        id_item_table = items['id']
        amount = items['amount']
        item_menu = get_item_menu(filepath, id_item_table)
        price = item_menu['price']

        subtotal += price * amount

    return {'subtotal': subtotal,
            'created_at': date_time}
