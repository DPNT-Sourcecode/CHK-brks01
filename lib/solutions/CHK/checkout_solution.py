

# noinspection PyUnusedLocal
# skus = unicode string
from typing import List, Tuple, Any, Optional
import re
from dataclasses import dataclass
from lib.solutions import utils

# (item, amount, special_offer, price_per_unit)
ITEM_OFFERS = {
    "A": ("A", 3, 130, 50),
    "B": ("B", 2, 45, 30),
    "C": ("C", None, None, 20),
    "D": ("D", None, None, 15),
}


def get_special_price(sku: str) -> Tuple[Any, Any, int]:
    """ Retrieve special offer cost if available
    """
    item = ITEM_OFFERS.get(sku, None)
    if not item:
        return 0, 0, 0
    return item[1], item[2], item[3]


def checkout(skus: str) -> int:
    """ Calculates total prices given skus strings
    Note:
        Translates skus into key-value where key is the SKU and value is the SKU count.
        Based on the special offers table, we apply necessary offers to SKUs that have special
        offers
    """
    if not isinstance(skus, str) or (len(skus) > 0 and not skus.isupper()):
        return -1

    container = utils.split_sku_str_number(skus)
    total = 0
    for item in container:
        tmp = get_special_price(item[0])
        if tmp[2] == 0:
            continue
        if tmp[0] and item[1] >= tmp[0]:
            #symbol
            discount = item[1] // tmp[0]
            non_discount = item[1] % tmp[0]
            total += ((discount*tmp[1]) + non_discount*tmp[2])
        else:
            total += (item[1]*tmp[2])

    return total


@dataclass
class Offer:
    free_special_offer_items: List[str] = []
    count: int
    base_price: int
    special_price: int

    def add_free_specials(self, symbol: str) -> None:
        self.free_special_offer_items.append(symbol)




@dataclass
class SKU:
    """
    Represents SKU item with corresponding offers if any
    Example: symbol: A, offers --> [(3,130), (5, 200)], count --> 2
            This SKU doesn't qualify for available discounts. count has to be 3 or more to qualify
    """
    symbol: str
    offers: List[Offer]
    count: int
    price: int

    def has_special_offers(self) -> bool:
        return len(self.offers) > 0

    def calculate_total_cost(self) -> int:
        if not self.has_special_offers():
            return self.count * self.price
        else:
            for offer in self.offers:







class SuperMarket:
    def __init__(self):
        pass

    def checkout(self, skus: str) -> int:
        """ Calculates total prices given skus strings
        Note:
            Translates skus into key-value where key is the SKU and value is the SKU count.
            Based on the special offers table, we apply necessary offers to SKUs that have special
            offers
        """







