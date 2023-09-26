from database.database import add_new_item
from src.stock_maganagment.stock_products import available_products


def stock_registration(destination_folder=None):
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

    if not destination_folder:
        available_products(destination_folder='reports')
        print('PDF was generated')
    else:
        available_products(destination_folder)


if __name__ == '__main__':
    stock_registration(destination_folder='../../reports')
