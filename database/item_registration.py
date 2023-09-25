from database.database import add_new_item


def stock_registration():
    # format: [(1, 'Coca-cola', 1.25)]

    product = tuple[int, str, float]

    while True:
        welcome = input('Do you want to add new items? Y/N ').lower()
        if welcome == 'n':
            break
        elif welcome == 'y':
            try:
                product_id = int(input('Enter the id of the item: '))
                product_name = input('Enter the name of the item: ')
                product_price = float(input('Enter the price of the item: '))
            except ValueError:
                print("Incorrect given values! ")
                continue

            product = (product_id, product_name, product_price)
            print(add_new_item([product]))  # to show messages
            continue


if __name__ == '__main__':
    stock_registration()
