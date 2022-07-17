

# noinspection PyUnusedLocal
# skus = unicode string
from typing import List, Tuple, Any, Optional
import re
# (item, amount, special_offer, price_per_unit)
ITEM_OFFERS = {
    "A": ("A", 3, 130, 50),
    "B": ("B", 2, 45, 30),
    "C": ("C", None, None, 20),
    "D": ("D", None, None, 15),
}


def get_special_price(sku: str) -> Tuple[Any, Any, int]:
    item = ITEM_OFFERS.get(sku, None)
    if not item:
        return 0, 0, 0
    return item[1], item[2], item[3]


def checkout(skus: str) -> int:
    if not isinstance(skus, str) or not skus.isalnum():
        return -1
    container = split_sku_str_number(skus.upper())
    total = 0
    for item in container:
        tmp = get_special_price(item[0])
        if tmp[2] == 0:
            continue
        if tmp[0] and item[1] >= tmp[0]:
            discount = item[1] // tmp[0]
            non_discount = item[1] % tmp[0]
            total += ((discount*tmp[1]) + non_discount*tmp[2])
        total += (item[1]*tmp[2])

    return total


def split_sku_str_number(skus: str) -> List[Tuple[str, int]]:
    results = [i for i in re.split(r"(\d+[A-Z]{1})|([A-Z])", skus) if i]
    modified_results = []
    for item in results:
        if len(item) == 1:
            modified_results.append((item, 1))
        else:
            modified_results.append((item[-1], int(item[:-1])))
    return modified_results








