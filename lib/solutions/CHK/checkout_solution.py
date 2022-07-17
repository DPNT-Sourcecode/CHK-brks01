

# noinspection PyUnusedLocal
# skus = unicode string
from typing import List
import re


def checkout(skus: str) -> int:
    return 0


def split_sku_str_number(skus: str) -> List:
    match = re.match("\d[A-Z]", skus)
    if match:
        items = match.groups()
    print(items)



