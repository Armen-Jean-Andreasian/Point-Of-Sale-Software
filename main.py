# pdf-related imports
from src.point_of_sales.pdf.current_time import Time
from src.point_of_sales.pdf.pdf_composer import PdfGenerator

# supermarket info-related imports
from src.supermarket_information.supermarket_customization import SupermarketDetails
from src.supermarket_information.customizing import customize

# stock-related imports
from src.stock_maganagment.product_registration import stock_registration
from src.stock_maganagment.stock_products import available_products

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


# Staff only. Adding new items to stock -----
def add():
    return stock_registration()


if __name__ == '__main__':
    while True:
        welcome = input('0 - Check available products\n'
                        '1 - Add items \n'
                        '2 - Check out products\n'
                        '3 - Edit supermarket information\n'
                        '4 - Exit the program\n'
                        'Your Choice: ')
        match welcome:
            case '0':
                available_products()
                break
            case '1':
                add()
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
