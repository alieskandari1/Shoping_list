from enum import Enum
from unicodedata import category


class CategoryEnum(Enum):

    categories = ("supermarket", "vegetables", "bakery", "fruits")
    supermarket = "supermarket"
    vegetables = "vegetables"
    bakery = "bakery"
    fruits = "fruits"
    trends = ("ascending", "descending")

