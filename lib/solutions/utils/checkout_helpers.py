import re
from typing import List, Tuple, Any



PRICE_TABLE = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

SPECIALS_PRICE_TABLE = {
    "A": [(3, 130), (5, 200)],
    "B": [(2, 45)],
    "E": [(2, -30)]
}


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


def get_offers(symbol: str) -> List[Any]:
    from lib.solutions.CHK.checkout_solution import Offer

    offers = SPECIALS_PRICE_TABLE.get(symbol, [])
    offer_container = []
    if not offers:
        return []
    else:
        for offer in offers:
            offer_container.append(Offer(discount_amount=offer[0], special_price=offer[1]))
    return sorted(offer_container, key=lambda itm: itm[0], reverse=True)


def get_sku_price(symbol: str) -> int:
    return PRICE_TABLE.get(symbol, 0)

