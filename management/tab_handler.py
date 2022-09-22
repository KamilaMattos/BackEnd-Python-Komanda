from datetime import datetime
from utils.json_handler import read_json


def get_item_menu(filepath: str, id_item_table: int):
    menu = read_json(filepath)

    for items in menu:
        if items['id'] == id_item_table:
            return items


def calculate_tab(table: list[dict], filepath: str):
    date_time_formated = '%d/%m/%Y, %H:%M:%S'
    subtotal = 0

    for items in table:
        id_item_table = items['id']
        amount = items['amount']
        item_menu = get_item_menu(filepath, id_item_table)
        price = item_menu['price']

        subtotal += price * amount

    return {'subtotal': subtotal,
            'created_at': datetime.now().strftime(date_time_formated)}
