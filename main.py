"""
Supermarket Point of Sale System

This module contains the implementation of a Point of Sale System (POS) for a supermarket. The system allows users
to check available products, add_product new items to stock, check out products, and edit supermarket information.
It also provides the functionality to generate PDF receipts for purchases.

Modules:
    - pdf-related imports
    - supermarket info-related imports
    - stock-related imports
    - point of sales-related imports

Global Variables:
    - current_time: The current time in 'HH:MM:SS' format.
    - current_day: The current date in 'YYYY-MM-DD' format.
    - supermarket_information: Details about the supermarket, including its logo, name, address, and operating hours.

Functions:
    - main: The main function that initiates the Point of Sale System.
    - add_product: Function to add_product new items to the stock.
"""

# pdf-related imports
from src.point_of_sales.pdf.current_time import Time
from src.point_of_sales.pdf.pdf_composer import PdfGenerator

# supermarket info-related imports
from src.supermarket_information.supermarket_customization import SupermarketDetails
from src.supermarket_information.customizing import customize

# stock-related imports
from src.stock_management.product_registration import stock_registration as add_product
from src.stock_management.stock_products import available_products

# point of sales-related imports
from src.point_of_sales.counter import BarcodeScanner

# Point of sales -----
current_time = Time.current_time()
current_day = Time.current_day()
supermarket_information = SupermarketDetails.get_supermarket_details()

pay_for_products = BarcodeScanner()  # input taking object


def main():
    local_receipt, local_total = pay_for_products.point_of_sales()  # input -> tuple[dict, float]

    pdf_generator = PdfGenerator(
        receipt=local_receipt,
        total=local_total,
        supermarket=supermarket_information,
        current_day=current_day,
        current_time=current_time
    )
    pdf_generator.start()


def start_point_of_sale():
    while True:
        welcome = input('0 - Check available products\n'
                        '1 - Add items\n'
                        '2 - Check out products\n'
                        '3 - Edit supermarket information\n'
                        '4 - Exit the program\n'
                        'Your Choice: ')
        match welcome:
            case '0':
                available_products()
                break
            case '1':
                add_product()
                print('Thanks for using POSS! Goodbye')
                break
            case '2':
                main()
                print('Thanks for using POSS! Goodbye')
                break
            case '3':
                customize()
                break
            case '4':
                print('Thanks for using POSS! Goodbye')
                break


if __name__ == '__main__':
    start_point_of_sale()
