

# noinspection PyUnusedLocal
# skus = unicode string
from typing import List, Union
import re


def checkout(skus: str) -> int:
    return 0


def split_sku_str_number(skus: str) -> List[Union[str, int]]:
    return [i for i in re.split(r"(\d+[A-Z]{1})|([A-Z])", "XYZ3BAT") if i]








