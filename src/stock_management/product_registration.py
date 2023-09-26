"""
Stock Registration: Utility module for registering and managing product stock.

This module provides functionality for adding new items to the product stock database
and generating stock reports in PDF format.

Functions:
    stock_registration: Interactive function to add_product new items to the product stock and generate stock reports.

Usage:
    The 'stock_registration' function allows users to interactively add_product new items to the product stock database.
    Users can specify whether to generate stock reports or not.

Examples:
    To add_product new items and generate stock reports:
    stock_registration(destination_folder='../../reports')

    To add_product new items without generating stock reports:
    stock_registration()

"""


from database.database import add_new_item
from src.stock_management.stock_products import available_products


def stock_registration(destination_folder=None):
    """
    Interactive function for adding new items to the product stock and generating stock reports.

    Args:
        destination_folder (str, optional): The destination folder for generating stock reports in PDF format.
            If not provided, the reports will be generated in the default folder. Defaults to None.

    Usage:
        To add_product new items and generate stock reports:
        stock_registration()

    Returns:
        None
    """
    # format: [(1, 'Coca-cola', 1.25)]

    product = tuple[int, str, float]

    while True:
        welcome = input('Do you want to add_product new items? Y/N ').lower()
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
        available_products(destination_folder='reports/stock_reports')
        print('PDF was generated')
    else:
        available_products(destination_folder)


if __name__ == '__main__':
    stock_registration(destination_folder='../../reports/stock_reports')
