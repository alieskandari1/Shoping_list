import pandas as pd
import csv

from constant import CategoryEnum


class Show:
    """
    this Class generally manages presentations
    of files and inventories in this app

    """

    def category_exist(self, csv_file: csv, category: str) -> bool:
        """
        get's the category name and searches the csv file
        if the category exists or not.
        our categories:
        "supermarket", "Vegetables", "bakery", "fruits"

        """
        self.category = category
        self.csv_file = csv_file

        with open(self.csv_file, 'r') as f:
            category_exist = False
            csv_reader = csv.reader(f, delimiter=",")
            for row in csv_reader:
                if row[0] == self.category:
                    category_exist = True
            return category_exist

    def show_warehouse(self):
        """
        show's warehouse inventory to shopkeeper

        """
        warehouse_reader = pd.read_csv("warehouse.csv")
        print(warehouse_reader)

    def Customer_receipts(self):
        """
        first check's witch category exists in the customers shoplist
        then iterates in it
        show's tha category,name and amount of products customer bought
        then show's the Total price

        prints
        ----------
        Customer receipts
        """

        price_list = list()

        with open("shop_list.csv", "r") as shoplist:
            reader = csv.reader(shoplist)
            print("\nsupermarket:")
            for row in reader:
                if row[0] == "supermarket":
                    print(f"{row[3]} {row[1]}'s\t Unit price: {row[2]} $ ")
                    total = float(row[2])*float(row[3])
                    price_list.append(total)

        with open("shop_list.csv", "r") as shoplist:
            reader = csv.reader(shoplist)
            print("\nVegetables:")
            for row in reader:
                if row[0] == "Vegetables":
                    print(f"{row[3]} {row[1]}'s\t Unit price: {row[2]} $")
                    total = float(row[2])*float(row[3])
                    price_list.append(total)

        with open("shop_list.csv", "r") as shoplist:
            reader = csv.reader(shoplist)
            print("\nbakery:")
            for row in reader:
                if row[0] == "bakery":
                    print(f"{row[3]} {row[1]}'s\t Unit price: {row[2]} $ ")
                    total = float(row[2])*float(row[3])
                    price_list.append(total)

        with open("shop_list.csv", "r") as shoplist:
            reader = csv.reader(shoplist)
            print("\nfruits:")
            for row in reader:
                if row[0] == "fruits":
                    print(f"{row[3]} {row[1]}'s\t Unit price: {row[2]} $ ")
                    total = float(row[2])*float(row[3])
                    price_list.append(total)

        total_amount = sum(price_list)
        print(f"\nTOTAL PRICE: {total_amount} $")

    def sorted_by_price(self, csv_file: csv, trend: str):
        """
        sorts the csv file content by the price of products

        Parameters
        ----------
        csv_file: csv

        trend: str :
        takes "a" for ascending trend,
        and takes "d" for descending trend.

        prints
        ----------
        sorted csv file content by the price of products
        """
        self.csv_file = csv_file
        self.trend = trend

        @property
        def trend(self):
            return self.__trend

        @trend.setter
        def trend(self, value):
            if isinstance(value, str):
                if value.isalpha():
                    if value in ("ascending", "descending"):
                        self.__trend = value.lower()
                    else:
                        raise ValueError(f"defined commands are:"
                                         " ascending and descending"
                                         f"entered command is:{value}")
                else:
                    raise ValueError(f"{value} has not alphabetic characters")
            else:
                raise ValueError(f"{value} must be a string")

        if self.trend == "a":
            csv_file = pd.read_csv(self.csv_file,
                                   usecols=["name", "count", "price"])
            print("\n your shopping list sorted by ascending price: ")

            csv_file.sort_values(by=["price"],
                                 axis=0,
                                 ascending=True,
                                 inplace=True)
            print(csv_file)

        elif self.trend == "d":
            csv_file = pd.read_csv(self.csv_file,
                                   usecols=["name", "count", "price"])

            print("\n your shopping list sorted by ascending price: ")

            csv_file.sort_values(by=["price"],
                                 axis=0,
                                 ascending=False,
                                 inplace=True)
            print(csv_file)

    def sorted_by_number_of_products(self, csv_file: csv, trend: str):
        """
        sorts the csv file content by the number of products

        Parameters
        ----------
        csv_file: csv

        trend: str :
        takes "a" for ascending trend,
        and takes "d" for descending trend

        prints
        ----------
        sorted csv file content by the number of products
        """
        self.csv_file = csv_file
        self.trend = trend

        if self.trend == "a":
            csv_file = pd.read_csv(self.csv_file,
                                   usecols=["name", "count", "price"])

            print("\n your shopping list sorted by"
                  " ascending number of products: ")

            csv_file.sort_values(by=["count"],
                                 axis=0,
                                 ascending=True,
                                 inplace=True)
            print(csv_file)

        elif self.trend == "d":
            csv_file = pd.read_csv(self.csv_file,
                                   usecols=["name", "count", "price"])

            print("\n your shopping list sorted"
                  " by ascending number of products: ")

            csv_file.sort_values(by=["count"],
                                 axis=0,
                                 ascending=False,
                                 inplace=True)
            print(csv_file)

    def warehouse_to_customer(self):
        """
        prints
        ----------
        warehouse products for the customer
        """
        warehouse_list = list()
        with open("warehouse.csv", "r") as warehouse:
            reader = csv.reader(warehouse)
            for row in reader:
                warehouse_list.append([row[0], row[1]])

            category_list = [i[1] for i 
                            in warehouse_list
                            if i[0] == "supermarket"]
            
            join_item = "\t".join(category_list)
            print("supermarket:")
            print(join_item)

            category_list = [i[1] for i 
                            in warehouse_list
                            if i[0] == "Vegetables"]

            join_item = "\t".join(category_list)
            print("\nVegetables:")
            print(join_item)

            category_list = [i[1] for i 
                            in warehouse_list
                            if i[0] == "bakery"]

            join_item = "\t".join(category_list)
            print("\nbakery:")
            print(join_item)

            category_list = [i[1] for i
                            in warehouse_list if
                            i[0] == "fruits"]

            join_item = "\t".join(category_list)
            print("\nfruits:")
            print(join_item)

    def total_number_of_products(self, csv_file: csv):
        """
        returns
        ----------
        total number of products in a csv file given to it

        """
        self.csv_file = csv_file
        total_number_list = list()
        with open(self.csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] == "count":
                    pass
                else:
                    total_number_list.append(int(row[3]))
        total_number = sum(total_number_list)
        return (total_number)

    def product_counter(self, csv_file: csv, product_name: str):
        """
        counts number of a product in a csv file

        returns
        ----------
        number of a product in a csv file
        """
        self.csv_file = csv_file
        self.product_name = product_name
        with open(self.csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == self.product_name:
                    product_count = (int(row[3]))
            return product_count

    def help(self):
        """
        print's first help of app
        """
        print("hello world")
        print("this is a shopping app,"
              "we will tell you how to use this app step by step"
              "\nfirst you have to choose your role 'shopkeeper' or 'customer'"
              "\nfor SHOPKEEPER enter == 'S'"
              "for CUSTOMER enter == 'C'"
              "\nfor help enter == 'HELP'"
              "\nto exit enter == 'DONE'")

    def help_shopkeeper(self):
        """
        print's shopkeeper help
        """
        print("as a shopkeeper you can use commands explained below:"
              "\nto View you warehouse inventory enter == VIEW"
              "\nto sort your inventory items by a special order enter == SORT"
              "\nto add or remove items from warehouse enter == EDIT"
              "\nto search among your products enter == SEARCH"
              "\nfor help enter == 'HELP'"
              "\nto exit enter == 'DONE'")

    def help_shopkeeper_edit(self):
        """
        print's shopkeeper edit help
        """

        print("to add a new product to warehouse enter == ADD"
              "\nto CHARGE a product enter == CH"
              "\nto DECREASE an existing product inventory enter == D"
              "\nto completely REMOVE product from warehouse enter == R"
              "\nfor help enter == 'HELP'"
              "\nto exit enter == 'DONE'")

    def help_customer(self):
        """
        print's customer help
        """
        print("as a customer you can use commands explained below:"
              "\nto buy enter == BUY"
              "\nto edit your shoplist enter == EDIT"
              "\nto view your shoplist enter == VIEW"
              "\nto sort your shopping list items"
              " by a special order enter == SORT"
              "\nto search among your products enter == SEARCH"
              "\nfor help enter == 'HELP'"
              "\nto exit enter == 'DONE'")
