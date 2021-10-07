"""
Author: Le Tuan Luc
Date: 2021/10/01
Program: IT19A2B_LeTuanLuc_49481_cau02.py
"""
product = []


class Product:
    def __init__(self, _id, _name, _qty, _price ) -> None:
        self.id = _id
        self.name = _name
        self.qty = int(_qty)
        self.price = int(_price)
    @property
    def payment(self):
        return self.qty * self.price


def is_product_empty():
    if product == []:
        print("You must import data from file input.txt first!")
        return True
    return False


def import_files():
    print("Importing from file input...")
    f = open("IT19A2B_LeTuanLuc_49481_inp.txt", 'r')
    for line in f:
        data_in_line = line.split("|")
        product.append(Product(data_in_line[0], data_in_line[1], data_in_line[2], data_in_line[3]))
    print("Done!")


def show_data():
    if not is_product_empty():
        print("{:^7} {:<10} {:^8} {:>10} {:>10}".format("ID", "Name", "Quantity", "Price", "Payment"))
        for data in product:
            print("{:^7} {:<10} {:^8} {:>10} {:>10}".format(data.id, data.name, data.qty, data.price, data.payment))


def show_the_higher_product_price():
    if not is_product_empty():
        max_price = 0
        for data in product:
            if data.price > max_price:
                max_price = data.price

        for data in product:
            if data.price == max_price:
                print("{:^7} {:<10} {:^8} {:>10} {:>10}".format(data.id, data.name, data.qty, data.price, data.payment))


def filter_product_quantity(number_of_quantity):
    if not is_product_empty():
        print("Creating file output...")
        f = open("IT19A2B_LeTuanLuc_49481_out.txt", "a")
        print("Exporting to file output...")
        for data in product:
            if data.qty >= number_of_quantity:
                f.write(f"{data.id}|{data.name}|{data.qty}|{data.price}|{data.payment}\n")
        print("Done!")


def main():
    print("\n", "="*5, " MENU ", "="*5)
    print("1. Import data from file input.txt")
    print("2. Show data")
    print("3. Show the highest product price")
    print("4. Export product qty>5 to output.txt")
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
            show_the_higher_product_price()
        if choice == 4:
            filter_product_quantity(5)
        if choice > 4:
            quit()
        main()
    except ValueError:
        print("Enter a positive number!")
        main()



if __name__ == "__main__":
    main()