
from item import Item
from display import Show
from warehouse import Store

display = Show()
store = Store()

display.help()
program_is_running = True
while program_is_running:

    role = input("\nselect your role:")

    if role.lower() == 'done':
        break

    elif role.lower() == 'help':
        display.help()

    elif role.lower() == "s":

        print("welcome to your shop\n")

        display.help_shopkeeper()
        role_is_shopkeeper = True
        while role_is_shopkeeper:
            command = input("\nenter your command:")

            if command.lower() == 'done':
                break

            elif command.lower() == 'help':
                display.help_shopkeeper()

            elif command.lower() == "search":
                command_is_search = True
                while command_is_search:
                    name = input("enter name of the"
                                 "product you want to search:")
                    if name == "done":
                        break
                    store.search("warehouse.csv", name)

            elif command.lower() == "view":
                display.show_warehouse()

            elif command.lower() == 'sort':
                command_is_sort = True
                while command_is_sort:
                    print(
                        "you can sort products"
                        " based on PRICE or NUMBER of them")

                    base = input("to sort by PRICE enter P"
                                 "\nto sort by NUMBER enter N:")
                    if base.lower() == "done":
                        break

                    elif base.lower() == "p":
                        trend = input("for ascending trend enter A"
                                      "\nfor descending trend enter D:")

                        if trend.lower() == "a":
                            display.sorted_by_price("warehouse.csv", "a")

                        elif trend.lower() == "d":
                            display.sorted_by_price("warehouse.csv", "d")

                    elif base.lower() == "n":
                        trend = input("for ascending trend enter A"
                                      "\nfor descending trend enter D:")
                        if trend.lower() == "a":
                            display.sorted_by_number_of_products(
                                "warehouse.csv",
                                "a")

                        elif trend.lower() == "d":
                            display.sorted_by_number_of_products(
                                "warehouse.csv",
                                "d")

            elif command.lower() == 'edit':
                display.help_shopkeeper_edit()
                command_is_edit = True
                while command_is_edit:
                    command = input("\nenter your command:")

                    if command.lower() == 'done':
                        break

                    elif command.lower() == 'help':
                        display.help_shopkeeper_edit()

                    elif command.lower() == 'add':
                        shopkeeper_is_adding = True
                        while shopkeeper_is_adding:
                            print("we have 4 categories in this shop:"
                                  "\nsupermarket\tVegetables\tbakery\tfruits")
                            category = input("select category of the product:")
                            if category.lower() == "done":
                                break
                            name = input("enter name of the product:")
                            if name.lower() == "done":
                                break
                            price = input("enter the price per unit:")
                            count = input(f"enter number of {name}:")

                            product = Item(category.lower(),
                                           name.lower(),
                                           price,
                                           count)
                            store.add_to_warehouse(product)
                            print(f"added {count} {name}'s to your warehouse")

                    elif command.lower() == 'ch':
                        shopkeeper_is_charging_stock = True
                        while shopkeeper_is_charging_stock:
                            name = input("enter name of the"
                                         "product you want to charge:")
                            if name.lower() == "done":
                                break

                            product_count = display.product_counter(
                                "warehouse.csv",
                                name)

                            count = input(
                                f"you have {product_count} {name}'s,"
                                f"\nenter number of {name} you want to add:")

                            if store.product_exist(
                                "warehouse.csv",
                                    name) is True:

                                store.charge_product(
                                    "warehouse.csv",
                                    name,
                                    count)

                                product_count = display.product_counter(
                                    "warehouse.csv", name
                                )

                                print(f"now you have {product_count}"
                                      "{name}'s in your warehouse ")

                            else:
                                print(
                                    f"you dont have any {name}"
                                    f" in the warehouse, add {name} first")

                    elif command.lower() == 'd':
                        shopkeeper_is_decreasing = True
                        while shopkeeper_is_decreasing:
                            name = input(
                                "enter name of the product"
                                " you want to decrease amount:")
                            if name.lower() == "done":
                                break

                            count = input(
                                f"enter number of {name}"
                                f"you want to decrease amount:")

                            if store.product_exist(
                                    "warehouse.csv", name) is True:

                                store.decrease_product(
                                    "warehouse.csv",
                                    name,
                                    count)

                                product_count = display.product_counter(
                                    "warehouse.csv", name)

                                print(
                                    f"now you have {product_count}"
                                    " {name}'s in your warehouse ")
                            else:
                                print(f"{name} doesn't exist")

                    elif command.lower() == 'r':
                        shopkeeper_is_removing = True
                        while shopkeeper_is_removing:
                            name = input(
                                "enter name of the product you want to remove:")
                            if name.lower() == "done":
                                break
                            store.remove_product(name)
                            print(f"{name} removed from your inventory")

    elif role == "c":
        print("welcome to our shop\n")
        display.help_customer()
        role_is_customer = True
        while role_is_customer:
            command = input("\nenter your command:")

            if command.lower() == 'done':
                break

            elif command.lower() == 'help':
                display.help_customer()

            elif command.lower() == 'search':
                customer_is_searching = True
                while customer_is_searching:
                    name = input(
                        "enter name of the product you want to search:")
                    if name.lower() == "done":
                        break
                    store.search("shop_list.csv", name)

            elif command.lower() == 'buy':
                print(
                    "These are the items you can choose."
                    "\nto stop buying enter == 'DONE'")
                display.warehouse_to_customer()
                customer_is_buying = True
                while customer_is_buying:
                    name = input(
                        "\nenter name of the product you want to buy:")
                    if name.lower() == 'done':
                        break
                    count = input(f"enter number of {name} you want to buy:")

                    if store.product_exist("shop_list.csv", name) is True:

                        product_count = display.product_counter(
                            "shop_list.csv", name
                        )

                        print(
                            f"you already have"
                            f" {product_count} {name}'s in your basket"
                            "\ndo you want add more?")

                        permision = input(
                            "for yes enter 'Y'"
                            "\nfor no enter 'N'")

                        if permision.lower() == "y":
                            store.buy(name, count)
                            product_count = display.product_counter(
                                "shop_list.csv", name
                            )
                            print(f"{count} {name}'s added to your basket,"
                                  f"now you have {product_count} {name}'s")
                        else:
                            pass

                    else:
                        store.buy(name, count)
                        product_count = display.product_counter(
                            "shop_list.csv", name
                        )
                        print(f"{count} {name}'s added to your basket,"
                              f"now you have{product_count} {name}'s")

            elif command.lower() == 'edit':
                command_is_edit == True
                while command_is_edit:
                    print(
                        "to DECREASE an existing product"
                        " inventory enter == D"
                        "\nto completely REMOVE product"
                        " from shoplist enter == R")

                    command = input("\nenter your command:")
                    if command.lower() == "done":
                        break

                    if command.lower() == 'd':
                        customer_is_decreasing = True
                        display.Customer_receipts()
                        while customer_is_decreasing:
                            name = input(
                                "enter name of the product"
                                " you want to decrease amount:")
                            if name.lower() == "done":
                                break

                            count = input(
                                f"enter number of {name}"
                                " you want to decrease amount:")

                            if store.product_exist(
                                "shop_list.csv", name
                            ) is True:

                                store.decrease_product(
                                    "shop_list.csv", name, count
                                )
                                product_count = display.product_counter(
                                    "shop_list.csv", name
                                )
                                print(f"{count} {name}'s removed from your basket,"
                                      f"now you have {product_count} {name}'s")
                            else:
                                print(f"{name} doesn't exist")

                    elif command.lower() == 'r':
                        customer_is_removing_product = True
                        display.Customer_receipts()
                        while customer_is_removing_product:
                            name = input(
                                "enter name of the product you want to remove:")
                            if name.lower() == "done":
                                break
                            store.delete_row("shop_list.csv", name)
                            print(f"deleted {name} from basket")
                            

            elif command.lower() == "view":
                display.Customer_receipts()

            elif command.lower() == 'sort':
                command_is_sort = True
                while command_is_sort:
                    print(
                        "you can sort products"
                        " based on PRICE or NUMBER of them"
                    )
                    base = input("to sort by PRICE enter P"
                                "\nto sort by NUMBER enter N:")

                    if base.lower() == "done":
                        break

                    if base.lower() == "p":
                        trend = input("for ascending trend enter A"
                                      "\nfor descending trend enter D:")

                        if trend.lower() == "a":
                            display.sorted_by_price("shop_list.csv", "a")

                        elif trend.lower() == "d":
                            display.sorted_by_price("shop_list.csv", "d")


                    elif base.lower() == "n":
                        trend = input("for ascending trend enter A"
                                      "\nfor descending trend enter D:")
                        if trend.lower() == "a":
                            display.sorted_by_number_of_products(
                                "shop_list.csv", "a")

                        elif trend.lower() == "d":
                            display.sorted_by_number_of_products(
                                "shop_list.csv", "d")