

# noinspection PyUnusedLocal
# skus = unicode string
from typing import List, Union
import re


def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1
    container = split_sku_str_number(skus)
    return 0


def split_sku_str_number(skus: str) -> List[Union[str, int]]:
    r = re.compile(r"(\d+[A-Z]{1})|([A-Z])|([A-Z]{1}\d+)")
    result = r.match(skus).groups()
    return [i for i in re.split(r"(\d+[A-Z]{1})|([A-Z])", "XYZ3BAT") if i]


