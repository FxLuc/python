"""
Author: Le Tuan Luc
Date: 2021/10/17
Program: IT19A2B_49481_LeTuanLuc_cau02.py
Note: Execute this file in the directory containing this file
"""
products = []


class Product:
    def __init__(self, _id, _name, _quantity, _price ) -> None:
        self.id = _id
        self.name = _name
        self.quantity = int(_quantity)
        self.price = int(_price)
    @property
    def total_money(self):
        return self.quantity * self.price


# check products[] is empty
def is_products_empty():
    if products == []:
        print("You must import product from file input.txt first!")
        return True
    return False


def import_files():
    print("Importing from file input.txt...")
    f = open("IT19A2B_49481_LeTuanLuc_inp.txt", 'r')
    for line in f:
        product_in_line = line.split("|")
        products.append(Product(product_in_line[0], product_in_line[1], product_in_line[2], product_in_line[3]))
    print("Done!")


def show_data():
    # make sure products[] is not empty
    if not is_products_empty():
        print("{:^7} {:<10} {:^8} {:>10} {:>15}".format("ID", "Name", "Quantity", "Price", "Total money"))
        for product in products:
            print("{:^7} {:<10} {:^8} {:>10} {:>15}".format(product.id, product.name, product.quantity, product.price, product.total_money))


def show_the_higher_products_price():
    # make sure products[] is not empty
    if not is_products_empty():
        max_price = 0
        for product in products:
            if product.price > max_price:
                max_price = product.price

        for product in products:
            if product.price == max_price:
                print("{:^7} {:<10} {:^8} {:>10} {:>15}".format(product.id, product.name, product.quantity, product.price, product.total_money))


def filter_products_quantity(number_of_quantity):
    # make sure products[] is not empty
    if not is_products_empty():
        print("Creating file output...")
        f = open("IT19A2B_49481_LeTuanLuc_out.txt", "a")
        print("Exporting to file output.txt...")
        for product in products:
            if product.quantity > number_of_quantity:
                f.write(f"{product.id}|{product.name}|{product.quantity}|{product.price}|{product.total_money}\n")
        print("Done!")


def main():
    print("\n", "="*5, " MENU ", "="*5)
    print("1. Import product from file input.txt")
    print("2. Show product")
    print("3. Show the highest product price")
    print("4. Export product quantity>5 to output.txt")
    print("Enter any number else to quit.")
    choice = input("Your choice: ")
    print()
    try:
        choice = int(choice)
        if choice == 1:
            import_files()
        if choice == 2:
            show_data()
        if choice == 3:
            show_the_higher_products_price()
        if choice == 4:
            filter_products_quantity(5)
        if choice > 4:
            quit()
        main()
    except ValueError:
        print("Enter a positive number!")
        main()



if __name__ == "__main__":
    main()