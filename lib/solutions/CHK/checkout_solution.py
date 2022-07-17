

# noinspection PyUnusedLocal
# skus = unicode string
from typing import List, Tuple
import re
# (item, amount, special_offer, price_per_unit)
ITEM_OFFERS = {
    "A": ("A", 3, 130, 50),
    "B": ("B", 2, 45, 30),
    "C": ("C", None, None, 20),
    "D": ("D", None, None, 15),
}


def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1
    container = split_sku_str_number(skus)
    return 0


def split_sku_str_number(skus: str) -> List[Tuple[str, int]]:
    results = [i for i in re.split(r"(\d+[A-Z]{1})|([A-Z])", skus) if i]
    modified_results = []
    for item in results:
        if len(item) == 1:
            modified_results.append((item, 1))
        else:
            modified_results.append((item[-1], int(item[:-1])))
    return modified_results







