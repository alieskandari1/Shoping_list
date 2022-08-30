from constant import CategoryEnum
from typing import List


class Item:

    def __init__(self, category: str, name: str, price: int, count: int):
        self.category = category
        self.name = name
        self.price = price
        self.count = count

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        category = CategoryEnum
        if isinstance(value, str):
            if value.isalpha():
                if value in category.categories.value:
                    self.__category = value.lower()
                else:
                    raise ValueError(
                        f"defined categories are: supermarket, Vegetables"
                        f",bakery and fruits. entered value is:{value}"
                    )
            else:
                raise ValueError(f"{value} has not alphabetic characters")
        else:
            raise ValueError(f"{value} must be a string")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if value.isalpha():
                self.__name = value.lower()
            else:
                raise ValueError(f"{value} has not alphabetic characters")
        else:
            raise ValueError(f"{value} must be a string")

    def get_item_list(self):
        """
        makes Item object attributes a list
        Returns
        -------
        list[Item]
        """

        return [self.category, self.name, self.price, self.count]

    def get_name(self):
        return f"item is {self.name}"

    def __str__(self) -> str:
        return self.get_name()

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, obj):
        return self.price == obj.price

    def __ne__(self, obj):
        return self.price != obj.price

    def __gt__(self, obj):
        return self.price > obj.price

    def __lt__(self, obj):
        return self.price < obj.price

    def __ge__(self, obj):
        return self.price >= obj.price

    def __le__(self, obj):
        return self.price <= obj.price

    def __add__(self, obj):
        return self.price + obj.price

    def __radd__(self, obj):
        return obj.price + self.price


