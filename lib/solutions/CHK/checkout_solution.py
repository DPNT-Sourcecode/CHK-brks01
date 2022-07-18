

# noinspection PyUnusedLocal
# skus = unicode string
from typing import List, Any
from dataclasses import dataclass
from lib.solutions.utils import checkout_helpers


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


@dataclass
class Offer:
    discount_amount: int
    special_price: int


@dataclass
class SKU:
    """
    Represents SKU item with corresponding offers if any
    Example: symbol: A, offers --> [(3,130), (5, 200)], count --> 2
            This SKU doesn't qualify for available discounts. count has to be 3 or more to qualify
    """
    symbol: str
    count: int
    price: int
    offers: List[Offer]
    sku_total_cost: int = 0

    def has_special_offers(self) -> bool:
        return len(self.offers) > 0

    def calculate_sku_total_cost(self) -> None:
        if not self.has_special_offers():
            self.sku_total_cost += (self.count * self.price)
        else:
            temp_count = self.count
            for offer in self.offers:
                discount_total = temp_count // offer.discount_amount
                non_discount_total = temp_count % offer.discount_amount
                if discount_total == 0:
                    continue
                else:
                    total = ((discount_total * offer.special_price) + (non_discount_total * self.price))
                    if offer.special_price < 0:
                        # free item offered, discount will apply to sku regular price
                        self.sku_total_cost += ((self.count * self.price) + total)
                    else:
                        self.sku_total_cost += total
                    temp_count -= offer.discount_amount


def get_offers(symbol: str) -> List[Any]:
    offers = SPECIALS_PRICE_TABLE.get(symbol, [])
    offer_container = []
    if not offers:
        return []
    else:
        for offer in offers:
            offer_container.append(Offer(discount_amount=offer[0], special_price=offer[1]))
    return sorted(offer_container, key=lambda itm: itm.discount_amount, reverse=True)


def get_sku_price(symbol: str) -> int:
    return PRICE_TABLE.get(symbol, 0)


class SuperMarket:

    def __init__(self, skus: str):
        self.skus: str = skus
        self.shopping_cart: List[SKU] = []

    def build_shopping_cart(self) -> None:
        cart = checkout_helpers.split_sku_str_number(self.skus)
        for item in cart:
            price = get_sku_price(symbol=item[0])
            offers = get_offers(symbol=item[0])
            sku = SKU(symbol=item[0], count=item[1], price=price, offers=offers)
            sku.calculate_sku_total_cost()
            self.shopping_cart.append(sku)

    def compute_checkout_cost(self) -> int:
        if not self.shopping_cart:
            return 0
        result = sum(item.sku_total_cost for item in self.shopping_cart)
        return result


def checkout(skus: str) -> int:
    """ Calculates total prices given List of SKUs
    """

    if not isinstance(skus, str) or (len(skus) > 0 and not skus.isupper()):
        return -1
    super_market = SuperMarket(skus=skus)
    super_market.build_shopping_cart()
    return super_market.compute_checkout_cost()



