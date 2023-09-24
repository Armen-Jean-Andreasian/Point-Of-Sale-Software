from src.current_time import Time
from src.supermarket_customization import SupermarketDetails
from src.pdf_composer import PdfGenerator
from src.counter import BarcodeScanner

current_time = Time.current_time()
supermarket_information = SupermarketDetails.get_supermarket_details()

barcode_scanner_on = BarcodeScanner()


def main():
    local_receipt, local_total = barcode_scanner_on.point_of_sales()

    pdf_generator = PdfGenerator(
        receipt=local_receipt,
        total=local_total,
        supermarket=supermarket_information,
        current_time=current_time
    )
    pdf_generator.start()


if __name__ == '__main__':
    main()
