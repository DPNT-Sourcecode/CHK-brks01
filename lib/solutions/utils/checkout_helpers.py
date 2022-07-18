import re
from typing import List, Tuple


def split_sku_str_number(skus: str) -> List[Tuple[str, int]]:
    """ Map sku character string with corresponding count
    """
    results = [i for i in re.split(r"(\d+[A-Z]{1})|([A-Z])", skus) if i]
    tmp = {}
    for item in results:
        if len(item) == 1 and item not in tmp:
            tmp[item] = 1
        elif len(item) > 1:
            if item[-1] not in tmp:
                tmp[item[-1]] = int(item[:-1])
            else:
                tmp[item[-1]] += int(item[:-1])
        else:
            tmp[item] += 1
    return list(zip(tmp.keys(), tmp.values()))