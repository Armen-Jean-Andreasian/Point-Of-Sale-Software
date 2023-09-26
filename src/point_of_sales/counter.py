"""
BarcodeScanner: Utility class for scanning product barcodes and generating receipts.

This module defines the BarcodeScanner class, which allows you to simulate a point of sale system.
It scans product barcodes, adds them to a receipt, and calculates the total sum of the purchase.

Classes:
    BarcodeScanner: Utility class for scanning product barcodes and generating receipts.

Methods:
    point_of_sales: Simulate a point of sale system, allowing the user to scan product barcodes and generate receipts.

Usage:
    The BarcodeScanner class provides a basic point of sale functionality for scanning product barcodes.
    You can use the 'point_of_sales' method to interactively scan barcodes and create receipts.

Examples:
    scanner = BarcodeScanner()
    receipt, total_sum = scanner.point_of_sales()

    # After scanning products, you can access the receipt and total sum.
    print("Receipt:", receipt)
    print("Total Sum:", total_sum)

"""


from database import database


class BarcodeScanner:
    receipt = dict()  # Should look like {'name': [10, 400.2], }
    total_sum = 0

    def point_of_sales(self) -> tuple[dict, float]:
        """
        Simulate a point of sale system, allowing the user to scan product barcodes and generate receipts.

        Returns:
            tuple: A tuple containing the receipt (a dictionary) and the total sum (a float).

        Usage:
            scanner = BarcodeScanner()
            receipt, total_sum = scanner.point_of_sales()

            # After scanning products, you can access the receipt and total sum.
            print("Receipt:", receipt)
            print("Total Sum:", total_sum)

        Raises:
            Exception: Raised for incorrect barcode input.

        Returns:
            tuple[dict, float]: A tuple containing the receipt (a dictionary) and the total sum (a float).
        """

        while True:
            id = input('Press \'f\' to stop. Enter id: ')
            if id == 'F'.lower():
                for key, value in self.receipt.items():
                    price = value[1]
                    self.total_sum += price

                break

            try:
                response = database.get_item_by_id(int(id))
                # response: [(12, 'Backpack (Nike)', 400.5)]

                item = response[0]
                product_name = item[1]
                product_price = item[2]

                if product_name not in self.receipt:

                    amount = 1
                    total = [amount, product_price]

                    self.receipt[product_name] = total

                elif product_name in self.receipt:
                    # receipt = {'name': [10, 400.2], }

                    item_total = self.receipt[product_name]

                    # updating amount
                    item_total[0] += 1

                    # updating total
                    item_total[1] += product_price

            except Exception:
                print('Incorrect id')

        return self.receipt, self.total_sum
