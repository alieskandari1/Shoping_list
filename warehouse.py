import csv

from item import Item
from logging import exception
from typing import List


class Store:
    """
    this Class generally manages all actions between warehouse and shoplist

    """
    
    def buy_permission(self, product_name: str, count: int) -> bool:
        """
        check's the warehouse that a product exists and counts it in
        Parameters
        ----------
        product_name :str

        count : get's the number of ordered product
        """
        self.product_name = product_name
        self.count = count

        with open('warehouse.csv', 'r') as f:
            x = False
            csv_reader = csv.reader(f, delimiter=",")
            for row in csv_reader:
                if row[1] == self.product_name:
                    if int(row[3]) == 0 or int(row[3]) - int(self.count) < 0:
                        x = False
                    elif int(row[3]) - int(self.count) >= 0:
                        x = True
            return x


    def delete_row(self, csv_file: csv, product_name: str) -> None:
        """
        this function get csv file and the product name
        and deletes product's row from the entered cdv file

        """

        self.csv_file = csv_file
        self.product_name = product_name
        lines = list()

        with open(self.csv_file, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == self.product_name:
                        lines.remove(row)

        with open(self.csv_file, 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    def append_row(self, csv_file: csv, append_list: List[Item]) -> None:
        """
        append's a row to the csv file you given

        """
        self.csv_file = csv_file
        self.append_list = append_list

        with open(self.csv_file, 'a', newline="") as shop_list_file:
            shop_list_file = csv.writer(
                shop_list_file,
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL)
            shop_list_file.writerow(self.append_list)


    def product_exist(self, csv_file: csv, product_name: str) -> bool:
        """
        check's if the product exists in the csv file you entered
        by searching name of it.

        """
        self.product_name = product_name
        self.csv_file = csv_file
        exist = False
        with open(self.csv_file, 'r') as f:
            csv_reader = csv.reader(f, delimiter=",")
            for row in csv_reader:
                if row[1] == self.product_name:
                    exist = True
            return exist

    def search(self, csv_file: csv, product_name: str):
        self.product_name = product_name
        self.csv_file = csv_file
        store = Store()

        if store.product_exist(self.csv_file, self.product_name) is True:
            with open(self.csv_file, 'r') as f:
                csv_reader = csv.reader(f, delimiter=",")
                for row in csv_reader:
                    if row[1] == self.product_name:
                        print(f"you have {row[3]} {row[1]}"
                            f",Unit price:{row[2]}$")
        else:
            print(f"{self.product_name} doesn't found")


    def buy(self, product_name: str, count: int) -> None:
        """
        first gets buy permission,
        then checks if product already exists in shoplist
        increase its amount, if not adds it to shoplist
        in both situations decreases product inventory in warehouse.csv

        Parameters
        ----------
        product_name: str

        count: int : number of product being ordered

        """
        self.product_name = product_name
        self.count = count
        add_to_shop_list = list()
        remove_list = list()
        store = Store()

        if store.buy_permission(self.product_name, self.count) is True:

            if store.product_exist('shop_list.csv',
                                    self.product_name) is True:

                with open('shop_list.csv', 'r') as f:
                    csv_reader = csv.reader(f, delimiter=",")
                    for row in csv_reader:
                        if row[1] == self.product_name:
                            row[3] = int(count) + int(row[3])
                            add_to_shop_list.append(row)

                store.delete_row("shop_list.csv", self.product_name)
                store.append_row("shop_list.csv", add_to_shop_list[0])

                with open('warehouse.csv', 'r') as f:
                    csv_reader = csv.reader(f, delimiter=",")
                    for row in csv_reader:
                        if row[1] == self.product_name:
                            row[3] = int(row[3]) - int(count)
                            remove_list.append(row)

                store.delete_row("warehouse.csv", self.product_name)
                store.append_row('warehouse.csv', remove_list[0])

            elif store.product_exist(
                                    "shop_list.csv",
                                    self.product_name) is not True:

                with open('warehouse.csv', 'r') as f:
                    csv_reader = csv.reader(f, delimiter=",")
                    for row in csv_reader:
                        if row[1] == self.product_name:
                            row[3] = int(count)
                            add_to_shop_list.append(row)

                with open('warehouse.csv', 'r') as f:
                    csv_reader = csv.reader(f, delimiter=",")
                    for row in csv_reader:
                        if row[1] == self.product_name:
                            row[3] = int(row[3]) - int(count)
                            remove_list.append(row)

                store.delete_row("warehouse.csv", self.product_name)
                store.append_row("shop_list.csv", add_to_shop_list[0])
                store.append_row('warehouse.csv', remove_list[0])
        else:
            raise exception(
                f"The stock of {self.product_name} has been exhausted")


    def add_to_warehouse(self, item: Item) -> None:
        """
        get's a object of Class Item then append that to the warehouse.csv

        """
        self.item = item
        if isinstance(self.item, Item):
            Store.append_row(self, "warehouse.csv", self.item.get_item_list())
        else:
            raise TypeError(f" {item} must be Item class type")


    def charge_product(self,
                    csv_file: csv,
                    product_name: str,
                    count: int) -> None:
        """
        increases product inventory in the given csv file
        by adding the number of existing product to the number given to it

        """
        self.csv_file = csv_file
        self.product_name = product_name
        self.count = count
        add_to_warehouse = list()
        store = Store()

        with open(self.csv_file, 'r') as f:
            csv_reader = csv.reader(f, delimiter=",")
            for row in csv_reader:
                if row[1] == self.product_name:
                    row[3] = int(count) + int(row[3])
                    add_to_warehouse.append(row)

        store.delete_row(self.csv_file, self.product_name)
        store.append_row(self.csv_file, add_to_warehouse[0])

    def decrease_product(self,
                        csv_file: csv,
                        product_name: str,
                        count: int) -> None:
        """
        decreases product inventory in the given csv file
        by Subtracting the number of existing product to the number given to it

        """
        self.csv_file = csv_file
        self.product_name = product_name
        self.count = count
        add_to_warehouse = list()
        store=Store()

        with open(self.csv_file, 'r') as f:
            csv_reader = csv.reader(f, delimiter=",")

            for row in csv_reader:
                if row[1] == self.product_name:
                    if int(row[3])-int(count) > 0:
                        row[3] = int(row[3]) - int(count)
                        add_to_warehouse.append(row)

                        store.delete_row(self.csv_file,
                                        self.product_name)

                        store.append_row(self.csv_file,
                                        add_to_warehouse[0])

                    else:
                        store.delete_row(self.csv_file,
                                        self.product_name)

    def remove_product(self, product_name: str) -> None:
        """
        get's the product name and completely deletes it from warehouse.csv
        """
        self.product_name = product_name
        store=Store()
        store.delete_row("warehouse.csv", self.product_name)



